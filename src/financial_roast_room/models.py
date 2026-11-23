"""Modèles structurés pour une session Financial Roast Room."""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class Stage(str, Enum):
    PROPOSALS = "proposals"
    CRITIQUES = "critiques"
    REVISIONS = "revisions"
    DECISIONS = "decisions"
    SYNTHESIS = "synthesis"


@dataclass
class Criterion:
    name: str
    weight: float


@dataclass
class InvestmentOption:
    name: str
    description: str


@dataclass
class Session:
    question: str
    context: str
    horizon: str
    criteria: list[Criterion]
    options: list[InvestmentOption]
    stage: Stage = Stage.PROPOSALS
    messages: list[dict[str, Any]] = field(default_factory=list)


@dataclass
class Proposal:
    agent: str
    option: str
    rationale: str
    risks: list[str]
    assumptions: list[str]


@dataclass
class Critique:
    agent: str
    target_agent: str
    points: list[str]


@dataclass
class Decision:
    agent: str
    choice: str | None
    rationale: str
    uncertainty: float
    minority_opinion: str = ""
