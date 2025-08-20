---
# layout: slide
title: Intro 
date: 2025-09-11
author: Alexia Schneider `alexia.schneider@umontreal.ca` (UdeM), 
  Marcello Vitali-Rosati `marcello.vitali.rosati@umontreal.ca` (UdeM)
bibliography: phd_udem.bib
link-citations: true
colorlinks: true
fig-cap-location: top
format:
    revealjs: 
        output-file: "intro.html" 
        # template: simple
        smaller: true
        incremental: true
        scrollable: true
        slide-number: true
---

## Plan 

1. Présentation de la série d'atelier 
2. Qu'est-ce que l'IA ? 
3. Intérêt d'étudier l'IA pour les SHS
4. Retours historiques
5. Typologie des IA
6. Cas d'usage et modélisation experte (ELIZA)
7. Cas d'usage et modélisation distributionnelle/vectorielle (vectorisation et prédiction)
8. Les LLMs
9. Usages des LLMs hors chatbots (demo)
10. LLMs et chatbots (Duck.ai + Ollama)
11. Conclusions

## Présentation et objectif des ateliers 

Format : 4 séances de 2heures, sans inscription, participation libre (à justifier pour le certificat des Humanités Numériques)

1h à 1h30 de théorie + 30 minutes à 1h de pratique.

Objectifs de la série d'atelier : 

- Comprendre les fondamentaux de l'IA et son histoire
- Obtenir des notions critiques sur le fonctionnement profond des outils
- Tester et s'approprier des outils d'IA 
- Maîtriser le vocabulaire de la discipline

Objectifs de cet atelier : 

- Comprendre les différentes formes d'IA
- Comprendre les enjeux liés à l'utilisation des LLM
- Utiliser de l'IA en dehors d'une interface de tchat.
- Tester les paramètres des chatbots
- Installer localement des modèles de langue.

## Qu'est ce que l'IA ? 

- Tout et rien : exemples : chatbot, détection sur des imageries médicales, HTR, DeepBlue. 

- le dernier mot à la mode. Le 'numérique' des années 2020. [@vitali-rosatiManifestePourEtudes2025]. 

## Qu'est-ce que l'IA ? 

Définition pratique : "un programme informatique qui effectue une prédiction." 

## L'IA et les SHS

À quoi sert d'étudier l'IA pour les chercheur.se.s en SHS ? 


## L'IA et les SHS

~~À quoi sert d'étudier l'IA pour les chercheur.se.s en SHS~~

## L'IA et les SHS

Que peuvent faire les SHS pour l'IA ? 

- participer à la réflexion actuelle sur son utilisation : 
    - positionnements de revues et de conférences sur son utilisation (pose un cadre, parfois un précédent)
- proposer une théorie critique de l'IA décentrées de l'effet 'benchmarking'
- proposer une avis sur l'utilisation de ces outils qui soit propre à sa discipline.


## Exemples de prises de position 

>Both SUP and JHUP have increasingly embraced, tested, and deployed some AI tools and policies. Barbara has been clear in her support of responsible uses of AI and the necessity of leveraging these early days to stake a claim within the quickly evolving landscape. Like SUP, JHUP is building and testing its own tools for marketing, accessibility, and analytics, efforts which place our presses in a position to potentially build services that might in the future even benefit other university presses. [@mulliken2025AUPressesWeekinResidence2025]

>we offer recommendations for citing generative AI, defined as a tool that “can analyze or summarize content from a huge set of information, including web pages, books and other writing available on the internet, and use that data to create original new content” (Weed). [@HowCiteGenerative2023]

> The uncomfortable truth for researchers and publishers who oppose AI slowly taking over human review is that they might not be able to prevent it. Should a researcher use AI to write the first pass of peer review and not disclose it — in contravention of publisher guidelines — that might not be detectable, says Hosseini, who is also one of the editors of the journal Accountability in Research. And if AI reviews become widespread, that could change the practice of science, says Priem. “Every researcher can run their own bespoke review service over the preprint/dataset landscape, flagging/extracting only the science they care about (at any “quality” level) they want that day,” he wrote on X earlier this year. That could start to eat into the roles of journals, by taking away the certification that peer review mediated by journals provides, he says.
[@naddafAITransformingPeer2025]


## Brève histoire de l'IA et des applications de linguistique computationnelle (pt. 1)

1940s : Science-fiction et roman d'Isaac Asimov _Runaround_ en 1942. 

@turingComputingMachineryIntelligence1950 : 'can machines think?'

'intelligence artificielle' : 1956 

>« The word Artificial Intelligence was then officially coined about six years later, when in 1956 Marvin Minsky and John McCarthy (a computer scientist at Stanford) hosted the approximately eight-week-long Dartmouth Summer Research Project on Artificial Intelligence (DSRPAI) at Dartmouth College in New Hampshire. » [@haenleinBriefHistoryArtificial2019, p. 7]

1966 : ELIZA [@weizenbaumELIZAComputerProgram1966]

1990-2000s : pic des systèmes experts et des arbres de décision. DeepBlue d'IBM [@campbellDeepBlue2002]. 


## Brève histoire de l'IA et des applications de linguistique computationnelle (pt. 2)

2010s : pic des systèmes d'IA avec une modélisation distributionnelle du language (vecteur). Word2Vec [@mikolovEfficientEstimationWord2013], GloVE [@penningtonGloVeGlobalVectors2014]. Parmi les avancées majeures de cette modélisation on compte le mécanisme d'attention [@vaswaniAttentionAllYou2017] et l'encodage bidirectionnel BERT [@devlinBERTPretrainingDeep2019] qui permettent des modèles très performants comme le GPT-3 d'OpenAI [@brownLanguageModelsAre2020]. 

Actuellement : tendance à l'hybridation [@marcusNextDecadeAI2020]

## Typologie de l'IA

- Approche experte : modélisation d'un programme à partir de **règles** précises. Les règles doivent être applicables à de nouvelles données pour faire une prédiction.

- Approche distributionnelle : modélisation d'un programme à partir d'un grand volume de données. Ce sont les **motifs de répétitions** qui permettent à la machine d'émettre une prédiction. 

## Ce qu'il faut retenir

- deux modélisations : une approche _top-down_ et une approche _sample-based_. 
- 'des saisons' en IA càd que certaines approches attirent l'attention à un moment donné, actuellement IA = chatbot voire ChatGPT. 
- l'IA réfère à des technologies variées et pas seulement à des programmes de génération textuelle. 









## Bibliographie
