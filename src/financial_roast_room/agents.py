"""Agents de démonstration déterministes pour exécuter le MVP sans fournisseur externe."""

from .models import Critique, Decision, Proposal, Session


class DeterministicAgent:
    def __init__(self, name: str):
        self.name = name

    def propose(self, session: Session) -> Proposal:
        option = session.options[0]
        return Proposal(
            agent=self.name,
            option=option.name,
            rationale=f"Cette option est proposée comme point de départ pour tester les critères de la session.",
            risks=["Les données utilisées sont limitées", "Le scénario futur reste incertain"],
            assumptions=["Les critères fournis représentent les priorités déclarées"],
        )

    def critique(self, session: Session, proposals: list[Proposal]) -> list[Critique]:
        critiques = []
        for proposal in proposals:
            if proposal.agent == self.name:
                continue
            critiques.append(Critique(
                agent=self.name,
                target_agent=proposal.agent,
                points=["Identifier les données vérifiables qui soutiennent cette proposition", "Comparer explicitement les risques aux critères pondérés"],
            ))
        return critiques

    def revise(self, session: Session, proposal: Proposal, critiques: list[Critique]) -> Proposal:
        if critiques:
            proposal.assumptions.append("Hypothèses à confirmer avec des sources datées")
            proposal.risks.append("Une proposition peut changer après vérification des données")
        return proposal

    def decide(self, session: Session, proposals: list[Proposal]) -> Decision:
        choice = proposals[0].option
        for proposal in proposals:
            if proposal.agent == self.name:
                choice = proposal.option
                break
        return Decision(
            agent=self.name,
            choice=choice,
            rationale="Choix provisoire fondé sur les critères déclarés ; validation des données requise.",
            uncertainty=0.6,
            minority_opinion="Toute option alternative doit rester visible dans la synthèse.",
        )
