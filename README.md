# Financial Roast Room

Prototyper une session est possible sans fournisseur de modèle ni dépendance externe :
plusieurs agents structurés passent par les étapes de proposition, critique, révision et décision,
puis la salle produit une synthèse traçable.

## Installation

```bash
python -m pip install -e .
```

## Exécution du démonstrateur

```bash
python -m financial_roast_room.cli
```

La sortie JSON présente les propositions, critiques, décisions, votes et un avertissement.
Ce démonstrateur est déterministe ; les agents ne prennent pas de décisions financières réelles.

## Tests

```bash
python -m unittest discover -s tests
```

## Implémentation du MVP

- Modèles Python pour la session, les critères, les propositions et les décisions.
- Orchestrateur contrôlant les phases du débat.
- Interface `Agent` permettant de remplacer les agents de démonstration par des fournisseurs de modèles.
- Agents déterministes pour valider le flux sans appel externe.
- Sortie structurée prête à être exposée par une future API.

## Garde-fous

Cette première version ne traite pas de données réelles ni n’exécute d’ordres.
Elle ne constitue pas un conseil financier personnalisé.
