"""Interface en ligne de commande du MVP."""

import json

from .agents import DeterministicAgent
from .models import Criterion, InvestmentOption, Session
from .orchestrator import RoastRoom


def main() -> None:
    session = Session(
        question="Quelle option offre le meilleur compromis selon mes critères ?",
        context="Simulation financière sans données marché vérifiées.",
        horizon="À définir avec l'utilisateur",
        criteria=[
            Criterion("rendement attendu", 0.4),
            Criterion("risque", 0.4),
            Criterion("liquidité", 0.2),
        ],
        options=[
            InvestmentOption("Option A", "Premier scénario de démonstration"),
            InvestmentOption("Option B", "Second scénario de démonstration"),
        ],
    )
    room = RoastRoom(session, [DeterministicAgent("Analyste fondamental"), DeterministicAgent("Gestionnaire du risque")])
    print(json.dumps(room.run(), indent=2, ensure_ascii=False))
