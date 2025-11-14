---
title: Automatiser la révision textuelle ? - Réunion plénière Revue3.0
date: 2025-11-20
author: Clara Grometto, Alexia Schneider
link-citations: true
colorlinks: true
fig-cap-location: top
bibliography: ../phd_udem.bib
format:
    revealjs: 
      theme: solarized
      smaller: true
      # incremental: true
      scrollable: true
      slide-number: true
      # show-slide-number: print
      output-file: "pres_atelier_AutomatisationCorr_PleniereRevue30.html"
---

## Amalgame entre révision et brouillonage (CG)

## Changements de paradigmes 

## Une question de système de valeurs (CG)
<!-- 

## La révision avant l'IA

> La rectification, sur le plomb, des erreurs commises par le compositeur, ainsi que l'exécution des changements apportés par l'auteur à la  composition du texte primitif sont connus sous la dénomination de correction. De, manière générale, ce mot s'emploie pour désigner toute  modification, quelle, qu'elle soit : ajoutés, suppressions, transpositions,  changements de texte, rectifications orthographiques, rappels de règles typographiques, etc. [@brossardCorrecteurTypographeRegles1924]

- Un savoir-faire qui nous vient du monde de l'imprimé
- Passer de la copie à l'ouvrage
- application des règles typographiques + reproduction fidèle et entière du manuscrit 
- un processus séquentiel (lecture → annotation → recomposition) 
- un processus itératif (premières, secondes épreuves, tierces)
- un processus collectif (auteur.ice → correcteur.ice → auteur.ice → compositeur.ice)


## Histoire de la correction automatique

Révision = _Grammar Error Correction_,  une tâche voisine de la Traduction Automatique : les technologies sous jacentes sont partagées

L'évaluation de la GEC et de la TA fait écho aux processus d'évaluation propre à la correction par un humain. 

Les premiers correcteurs automatiques se sont concentrés sur la correction ortho-typographiques, mais les systèmes experts sont en réalité dépassés par la complexité de la langue naturelle.

Avec le développement des approches inductives, on aperçoit un premier changement de paradigme depuis la fin des années 2000 : correction = reformulation et plus seulement ortho-typographie.

Avec l'ancrage de nouvelles "pratiques discrètes" [@mullerPoussiereLumiereBleue2021] de l'IA , on assiste à une nouvelle phase : la correction comme écriture mais aussi comme masquage de l'utilisation d'IA générative. 

Les directives des maisons d'édition sont souvent floues, mais énoncent que la correction fait partie des utilisations acceptées, mais où s'arrête la correction?

Voir l'atelier IA sur la correction animés [@gromettoDebogueTesHumanites2025]
 -->
# Risques et limites à l'utilisation de LLM pour la correction 


## Homogénéisation de la langue (CG + AS)

1. le LLM reflète des données d'entraînement mais aussi les phases de _reinforcement learning_ qui l'oriente vers certains comportements standards porteurs de normes (ex: Français parisien) [@lodgeFrenchDialectStandard1993].
2. S'il est possible de demander à un LLM de changer son comportement, il est ramené vers ses paramètres généraux : c'est "l'attraction par défaut" [@paschalidisVersLangageSans2025]. 
3. La portion croissante de données synthétiques dans les jeux d'entraînement de ses modèles renforce leurs biais (perte de diversité) et rends les réponses des modèles moins fiables (effondrement). 

##  Un idéal de clarté qui finit par s’auto-parodier (le fameux *style chatgpt*) (CG)

> We show that while the core content of texts is retained when LLMs polish and rewrite texts, **not only do they homogenize writing styles, but they also alter stylistic elements in a way that selectively amplifies certain dominant characteristics or biases while suppressing others - emphasizing conformity over individuality**. By varying LLMs, prompts, classifiers, and contexts, we show that these trends are robust and consistent. 
[@sourati2025shrinkinglandscapelinguisticdiversity]

## Effet nivelant et autorité de la machine ? (AS)

La délégation de la tâche de relecture et des tâches associées à la correction (traduction, mise en page) a un effet nivelant. 

Les moins bons traducteurs sont aidés par la TA mais les meilleurs traducteurs sont désavantagés par la TA. Effet limitant car tendance à se laisser influencer : réduction des intuitions de traduction et de la créativité traductionnelle. [@schumacherPosteditionTraductionAutomatique2023]

La délégation cognitive et l'influence que ces machines ont sur nous individuellement n'est pas négligeable (voir @vicenteHumansInheritArtificial2023). 

## Quelle productivité ? (CG)

**Les outils incarnent une vision du monde centrée sur la productivité et la rapidité**

Assiste-t-on a une déprise tu texte et à une déprise du sens ? Existe-t-il un seuil, une limite, au-delà de laquelle le recours aux LLMs constitue une perte de maîtrise du texte ?

Les promesses de gain de temps et de productivité cachent des enjeux économiques forts : on ne peut que rester méfiants tant face aux biais de ces outils qu'à notre propension à être influencé par ses outils. 

## Pour en savoir plus 

Voir l'atelier IA sur la correction animé par [@gromettoDebogueTesHumanites2025]

## Questions  

Quels outils utilisez vous pour la correction des textes ? 

Est-ce que vous constatez un gain de temps ou est-ce qu'il faut relire le relecteur automatique aussi ? 

Est-ce que vous constatez que les corrections proposées 'améliorent' ou 'amoindrissent' la qualité du texte que vous comptez publier ?

Est-ce que les fonctionnalités de 'détection de textes générés par IA' vous aident/aideraient dans vos travaux (enseignement, édition, peer review) ?


## Bibliographie




