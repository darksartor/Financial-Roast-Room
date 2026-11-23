"""Orchestration déterministe des étapes du débat."""

from collections import Counter
from typing import Protocol

from .models import Critique, Decision, Proposal, Session, Stage


class Agent(Protocol):
    name: str

    def propose(self, session: Session) -> Proposal: ...
    def critique(self, session: Session, proposals: list[Proposal]) -> list[Critique]: ...
    def revise(self, session: Session, proposal: Proposal, critiques: list[Critique]) -> Proposal: ...
    def decide(self, session: Session, proposals: list[Proposal]) -> Decision: ...


class RoastRoom:
    def __init__(self, session: Session, agents: list[Agent]):
        if not session.options:
            raise ValueError("Au moins une option d'investissement est requise")
        if not session.criteria:
            raise ValueError("Au moins un critère de décision est requis")
        total = sum(criterion.weight for criterion in session.criteria)
        if abs(total - 1.0) > 1e-9:
            raise ValueError("La somme des pondérations doit être égale à 1")
        if not agents:
            raise ValueError("Au moins un agent est requis")
        self.session = session
        self.agents = agents

    def run(self) -> dict:
        proposals = self._collect_proposals()

        self.session.stage = Stage.CRITIQUES
        critiques = self._collect_critiques(proposals)

        self.session.stage = Stage.REVISIONS
        revised = self._collect_revisions(proposals, critiques)

        self.session.stage = Stage.DECISIONS
        decisions = self._collect_decisions(revised)

        self.session.stage = Stage.SYNTHESIS
        return self._synthesize(revised, critiques, decisions)

    def _collect_proposals(self) -> list[Proposal]:
        proposals = [agent.propose(self.session) for agent in self.agents]
        self.session.messages.append({"stage": Stage.PROPOSALS.value, "items": [p.__dict__ for p in proposals]})
        return proposals

    def _collect_critiques(self, proposals: list[Proposal]) -> list[Critique]:
        critiques = [critique for agent in self.agents for critique in agent.critique(self.session, proposals)]
        self.session.messages.append({"stage": Stage.CRITIQUES.value, "items": [c.__dict__ for c in critiques]})
        return critiques

    def _collect_revisions(self, proposals: list[Proposal], critiques: list[Critique]) -> list[Proposal]:
        revised = []
        for proposal in proposals:
            agent = next(agent for agent in self.agents if agent.name == proposal.agent)
            related = [critique for critique in critiques if critique.target_agent == proposal.agent]
            revised.append(agent.revise(self.session, proposal, related))
        self.session.messages.append({"stage": Stage.REVISIONS.value, "items": [p.__dict__ for p in revised]})
        return revised

    def _collect_decisions(self, proposals: list[Proposal]) -> list[Decision]:
        decisions = [agent.decide(self.session, proposals) for agent in self.agents]
        self.session.messages.append({"stage": Stage.DECISIONS.value, "items": [d.__dict__ for d in decisions]})
        return decisions

    def _synthesize(self, proposals: list[Proposal], critiques: list[Critique], decisions: list[Decision]) -> dict:
        votes = Counter(decision.choice for decision in decisions if decision.choice is not None)
        return {
            "question": self.session.question,
            "stage": self.session.stage.value,
            "criteria": [criterion.__dict__ for criterion in self.session.criteria],
            "proposals": [proposal.__dict__ for proposal in proposals],
            "critiques": [critique.__dict__ for critique in critiques],
            "decisions": [decision.__dict__ for decision in decisions],
            "votes": dict(votes),
            "result": max(votes, key=votes.get) if votes and len(set(votes.values())) > 1 else None,
            "disclaimer": "Analyse informative, sans conseil financier personnalisé ni garantie.",
        }
