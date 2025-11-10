---
title: Projet IEML -  Un système de recommandation basé sur différentes stratégies de recherche d'information exploratoire
author: Alexia Schneider `alexia.schneider@umontreal.ca` (UdeM)
date: 2025-11-19
bibliography: ../phd_udem.bib
link-citations: true
colorlinks: true
fig-cap-location: bottom
format:
    revealjs: 
        output-file: "presentationProjetIEML.html" 
        # template: simple
        smaller: true
        # incremental: true
        scrollable: true
        slide-number: true
---

## Plan

Contexte et présentation du projet 

- état actuel des systèmes de RI et les RS : 
    - problème de l'explicabilité 
- Solution développée
    - un RS hybride pour l'explicabilité 


## Contexte du projet


Les moteurs de recherche et bases de données scientifiques :

- proposent des articles « similaires » sans expliquer les critères de rapprochement.
- s’appuient sur :
    - le nombre de citations (Matthew's effect) [@desollapriceLittleScienceBig1963; @mertonMatthewEffectScience1968], 
    - des algorithmes de classement favorisant les articles déjà populaires (ranking) et les auteurs les plus cités [@cardonDansLespritPageRank2013]. 
    - les intéractions précédentes des utilisateur.ice.s. [@kosterSerendipitousRecommendationBased2014]

[Page d'exemple sur Isidore](https://isidore.science/document/20.500.13089/k0dm) 


## Problématique

Ces logiques entraînent :

Une concentration des citations et une perte de diversité scientifique. 

Des **bulles de filtres** [@pariserFilterBubbleWhat2011] et un **biais de confirmation** dans la recherche [@underwoodTheorizingResearchPractices2014]. 


## Les AI research assistant

Les moteurs de recherche académiques développent des méthodes de RI basées sur l'IA : 

- _Query augmentation_ 
- _semantic search_ ou recherche vectorielle
- (re)ranking 

Les articles proposés par ces _recommender systems_ (RS) peuvent varier en fonction de la stratégie sous-jacente : quid de la reproductibilité et de l'explicabilité [@tayReproducibilityInterpretabilityAcademic2025] ?

## Questions de recherche

Comment concevoir un système de recommandation explicable qui :

Favorise la sérendipité et l’exploration critique ?

Compare IA symbolique et IA connexionniste ?

Permette une visualisation réflexive du raisonnement algorithmique ?

# Proposition 

## Un RS hybride 

Un RS qui vient s'ajouter aux moteurs de recherche de publications scientifiques et proposer une exploration de la littérature scientifique de façon explicable et non-déterministe, en comparant les recommandations basées sur :

- des ontologies symboliques (IEML)
- des modèles connexionnistes (LLM)


## Objectif

Produire un RS explicable qui valorise la recherche exploratoire de l'utilisateurice sans imposer une méthode. 

Permettre de décloisonner le jargon. 

Proposer un outil pour une litéracie du numérique et particulièrement une littératie critique de l'IA 
[@goodladEditorsIntroductionHumanities2023; @vitali-rosatiManifestePourEtudes2025a] en se concentrant sur l'explicitation des stratégies de recherche d'information [@julienHowHighschoolStudents2009]. 


## IEML comme base ontologique 

Langage sémantique de Pierre Lévy [@levySocialComputingReflexive2010] :

Vocabulaire contrôlé et non ambigu

Chaque concept est décomposé selon 9 rôles sémantiques :
`thème, qui, quoi, à qui, par quoi, quand, où, pourquoi, comment`

Interopérable et explicable qui permet une navigation non-linéaire dans les concepts


# Démonstration


## Méthodes d’implémentation 

Parsing sémantique : via LLM + dictionnaire IEML (RAG)

Recherche sémantique : embeddings pour la similarité

Interface : JavaScript / HTML / API Isidore

Tests : intégration Firefox puis Chrome


## Schéma du fonctionnement 

![Processus de recommandation hybride](recommendation_systems-1.png)

Bleu = IEML

Orange = LLM

Vert = Actions utilisateur

→ L’utilisateur explore, sélectionne, et compare les résultats des deux approches

![Visualisation côte-à-côte des suggestions via les logs IEML et le 'semantic search' ](img/etape5_affichageArticles.png)


## Défis et perspectives

1. Traduction IEML:
- Avantage : flexibilité dans la définition, pas de “gold standard” : évaluation possible par des métriques sans référence (perplexité, distance cosinus)
- RAG sur le dictionnaire de ~3000 entrées IEML
- Évaluation humaine (Pierre Lévy)

2. Interaction avec les plateformes : API Isidore accessible, Google Scholar non garantie

3. Conception UX/UI 
- "interface intuitive" vs. logique intempestive
- Équilibre entre documentation et liberté

4. Intérêt fondamental 
- Évaluation utilisateur : entretiens « think aloud » pour mesurer la valeur pédagogique
- Comment observer si l’outil déclenche de nouvelles associations sémantiques ?


## Bibliographie

::: {#refs}
:::

# Merci pour votre attention ! 


---

![](img/etape1_extractionKeywords.png)

---


![](img/etape2_selectionConcepts.png)

---

![](img/etape3_selectionConceptsAssocies.png)

---

![](img/etape4_selectionHistorique.png)

---

![](img/etape5_affichageArticles.png)










