# Financial Roast Room

Un espace de débat où plusieurs agents IA analysent une question d’investissement depuis des perspectives différentes, critiquent les propositions adverses, puis rendent chacun une décision motivée. Le résultat est une comparaison structurée des options — pas une promesse de rendement ni un conseil financier personnalisé.

## Objectif

Aider l’utilisateur à examiner une décision financière en faisant apparaître les arguments, les hypothèses, les risques et les désaccords que pourrait manquer une analyse unique. La « meilleure » proposition est celle qui ressort selon les critères définis pour la session ; elle n’est jamais présentée comme universellement optimale ou garantie.

## Déroulement d’une session

1. **Question et contexte** — l’utilisateur décrit la décision, l’horizon, les contraintes et les critères de comparaison. Les informations personnelles non nécessaires ne sont pas demandées.
2. **Propositions indépendantes** — chaque agent prépare une analyse avant de voir celles des autres, afin de limiter l’effet de groupe.
3. **Roast contradictoire** — les agents contestent les hypothèses et arguments des propositions, sans attaque personnelle. Chaque critique doit être précise et justifiée.
4. **Réponse et révision** — les agents répondent aux critiques, corrigent si nécessaire leurs hypothèses et peuvent modifier leur proposition.
5. **Décision individuelle** — chaque agent évalue les options avec les mêmes critères, explique son choix et indique son niveau d’incertitude.
6. **Synthèse** — l’application présente les décisions, les arguments majoritaires et minoritaires, les risques, les hypothèses et les questions restant à vérifier.

## Agents envisagés

Les rôles sont complémentaires, pas des personnes ni des experts certifiés :

- **Analyste fondamental** — examine les fondamentaux, la valorisation et les hypothèses de croissance.
- **Analyste macroéconomique** — considère les taux, l’inflation, les cycles et les facteurs géopolitiques pertinents.
- **Gestionnaire du risque** — cherche les risques de perte, la concentration, la liquidité et les scénarios défavorables.
- **Avocat du diable** — construit le meilleur argument contre chaque proposition et vérifie les angles morts.
- **Synthétiseur / modérateur** — applique les règles de débat, fait respecter les tours et rassemble les éléments sans effacer les désaccords.

Les agents doivent distinguer les faits vérifiables des hypothèses et opinions, citer les sources disponibles avec leur date, signaler les données manquantes et éviter d’inventer des chiffres.

## Principes de décision

- Les critères et leur pondération sont visibles et définis avant le vote.
- Les agents rendent leur décision finale indépendamment après le débat.
- Une décision inclut arguments pour et contre, risques, hypothèses, horizon et incertitude.
- Le résultat expose les votes et les désaccords ; une moyenne ou une majorité ne constitue pas une preuve de justesse.
- Si les informations sont insuffisantes ou les avis trop incertains, la conclusion peut être « aucune proposition ne se démarque ».
- Les performances passées ne garantissent pas les performances futures.

## MVP proposé

1. Créer une session avec une question et des critères de comparaison.
2. Lancer un petit groupe d’agents à rôles configurés.
3. Afficher les tours de proposition, critique, réponse et décision.
4. Présenter un tableau comparatif final avec votes, justifications, risques et désaccords.
5. Permettre de consulter et partager une session.

À exclure du MVP : exécution d’ordres, connexion à un compte de courtage, recommandations personnalisées d’achat/vente et promesses de rendement.

## Architecture fonctionnelle proposée

- **Interface** : création de session, progression du débat, comparaison finale et historique.
- **Orchestrateur** : machine à états contrôlant les tours, les délais, les erreurs, les limites de coût et les règles de fin.
- **Agents** : rôles et consignes configurables, avec sorties validées selon un schéma commun.
- **Sources de données** : intégrations explicites et traçables ; chaque donnée externe est accompagnée de sa source et de son horodatage.
- **Persistance** : sessions, messages, décisions, critères et références, avec contrôle d’accès et politique de conservation.

Une implémentation devrait commencer par une orchestration séquentielle et des sorties structurées ; elle pourra évoluer vers des débats plus dynamiques après validation de la fiabilité et des coûts.

## Garde-fous

- Afficher clairement que les agents peuvent se tromper et que le contenu est informatif, non un conseil financier personnalisé.
- Ne pas laisser un agent exécuter des transactions ni accéder à des identifiants de courtage.
- Ne pas inventer de cotations, de sources ou de données financières ; indiquer explicitement quand les données ne sont pas disponibles ou à jour.
- Séparer les faits, les hypothèses et les opinions ; conserver les avis minoritaires dans la synthèse.
- Protéger les questions et données des utilisateurs, limiter leur collecte et ne pas les réutiliser sans consentement.
- Prévoir une revue des obligations légales et réglementaires applicables avant toute mise à disposition publique.

## État du projet

Le dépôt démarre avec la définition produit et le périmètre du MVP. La pile technique et les fournisseurs de modèles restent à choisir avant l’implémentation.
