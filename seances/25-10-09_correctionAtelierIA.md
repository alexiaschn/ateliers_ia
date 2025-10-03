---
title: 2e séance atelier IA  - révision et correction automatique
prof: Alexia Schneider + Clara Grometto
date: 9 octobre 2025
bibliography: ../correction.bib
link-citations: true
colorlinks: true
fig-cap-location: top
format:
    revealjs: 
        output-file: "correction.html" 
        # template: simple
        smaller: true
        incremental: true
        scrollable: true
        slide-number: true
---
## Plan de l'atelier

Théorie :


1. Rappels sur les fondements de l'IA 
2. Problématique et annonce du plan (CG)
3. Mise en perspective
4. Définition 
5. Présentation historico-technique des systèmes de GEC (AS) 
6. Changement de paradigme : de l'ortho-typo à la reformulation voire la génération de contenu 
7. Enjeux/conséquence (questions) 
    - gain de temps 
    - uniformisation de la langue
    - système de valeurs 
    - influence de la machine
8. Présentation des outils
9. conclusion/ce qu'il faut retenir (5min)

# Introduction

## Présentation et objectif des ateliers 

Format : 4 séances de 2heures, sans inscription, participation libre (à justifier pour le certificat des Humanités Numériques)

Théorie et pratique. 

Objectifs de la série d'atelier : 

- Comprendre les fondamentaux de l'IA et son histoire
- Obtenir des notions critiques sur le fonctionnement profond des outils
- Tester et s'approprier des outils d'IA 
- Maîtriser le vocabulaire de la discipline

Objectifs de cet atelier : 

- Cerner un cas d'usage courant des IA génératives : la correction ortho-typographique.
- S'interroger sur l'impact de ces nouvelles pratiques dans le travail de recherche.  
- Tester et comparer des outils courants. 
- Définir des critères pour effectuer un choix éclairé vis-à-vis des outils disponibles. 


## Certificat canadien en Humanités Numériques

![Certificat canadien en HN](/seances/img/ccdhn1.png)

![Certificat canadien en HN](/seances/img/ccdhn2.png)
![Certificat canadien en HN](/seances/img/ccdhn3.png)

[Information sur le certificat](https://ccdhhn.ca/)

# Les fondamentaux : rappels de l'introduction


## Qu'est ce que l'IA ? 
 
Des programmes informatiques que nous estimons à la hauteur de l'intelligence humaine ? Le développement des technologies fait évoluer cette définition de l'_intelligence_ non seulement _artificielle_ mais aussi _humaine_.

'IA' depuis 5 ans, a remplacé le 'numérique' des années 2010, et le 'cyberespace' des années 1990 et 2000.[@vitali-rosatiManifestePourEtudes2025]. 

Définition pratique pour ces ateliers: "un programme informatique qui effectue une prédiction."

## Rappels de l'introduction

- Les programmes d'IA réfèrent à des processus algorithmiques variés et pas seulement à des chatbots type ChatGPT.
- L'IA est une discipline qui a plus de 75 ans (terme de 1956). 
- [@turingComputingMachineryIntelligence1950] a orienté la discipline vers un modèle 'chatbot'.
<!-- ici expliquer Turing :  l'article Computing machinery intelligence a orienté la discipline vers une définition étroite de l'intelligence humaine comme intelligence sociale, ou capacité à feindre un échange social comme preuve d'humanité -->
- Les 'saisons de l'IA' suivent des phases d'approbation publique et de désintérêt pour le terme et les technologies qu'on place sous ce terme.
- Ce qu'on fait entrer dans la catégorie d'"intelligent" a changé : le calcul savant est-il moins intelligent que le bavardage ? 


## Rappels historiques sur l'IA

- Deux grandes approches en IA : une approche déductive (IA symbolique, système expert) vs. approche inductive (IA connexionniste, modèle de langue). 
- Un système expert peut être aussi complexe et énergivore qu'un LLM.
- Un LLM (_large language model_) est la modélisation sous forme de vecteurs de chaque élément d'un grand corpus (_token_ ~mot) par rapport à cet ensemble. 

[Démo visuelle](https://demo-atelier.streamlit.app/)

## Les LLMs en contexte

- Concernant les LLMs : systèmes d'IA n'ont pas de connaissance du réel ou de 'compréhension' : les réponses sont probabilistes. 
- Les hallucinations ne sont pas des anomalies, ce sont des erreurs que l'on qualifie a postériori comme telle. 
- Après l'apprentissage de son corpus d'entrainement, une étape de _reinforcement learning_ donne une saveur ou personnalité à un modèle.
- Les LLMs reflètent les intérêts économiques de leurs concepteurices: nature 'sycophantique' avérée. 
- On peut influencer le calcul de probabilité d'un modèle (température, top-k, seed)
- On peut aussi 'orienter' le comportement d'un modèle avec un _system prompt_.  
- Chatbots  = interfaces en langue naturelle : l'exploitation des capacités inductives d'un LLMs ne nécessite pas de passer par une telle interface. Ex : classification avec de l'apprentissage machine (_machine learning_). 


# La correction à l'heure de l'IA générative

## Changement de paradigme

Avant les LLM, les outils de 'corrections' sont spécialisés pour la correction ortho-typographique.   Maintenant les outils de correction dépassent les limites de la simple correction grammaticale.

- Reformulation.
- Génération de texte. 
- Masquer l'utilisation d'une IA. 


## Quelle définition de la correction ?

<!-- peut-être proposer des exemples, prendre son temps ? -->
- une étape négligée ou dévaluée ? quelle place dans notre système de valeurs ? 
- qu'est-ce qui entre réellement dans cette étape ? 
    - corrections orthographiques, 
    - corrections typographiques,
    - vérification de la mise en page,
    - traduction, 
    - vérification des sources, 
    - amélioration du style, ton. 
    - reformulation selon le lectorat pressenti (prise en compte de la situation d'énonciation)

    <!-- répétition, niveau de langue, terminologie, alléger les phrases -->
    - amélioration du contenu. 
    
La correction bibliographique : 'la barrière du dernier kilomètre' [@monjourBarriereDernierKilometre2025] 




## Qu'est-ce que la relecture-correction ?

- correction ortho-typo
- des énoncés grammaticalement justes ⇒ la grammaire c’est que des règles de combinaison, purement syntaxique, combinatoire sans sémantique. Règles systématiques et productives. Computation de séquences.
- des énoncés qui font sens ⇒ sémantiquement correctes
- adéquation avec une situation d’énonciation ⇒ implique la pragmatique
- le style qui flirt avec les limites du correct
- la reformulation c’est encore autre chose


## Les étapes de la correction


1. la lecture 
2. établir des critères de corrections : orthographe = règles de la langue, mais style etc.
3. l'annotation = proposition
4. la réécriture


**La correction est un processus itératif : c'est déjà une forme d'évaluation**


<!-- ## De l'importance du versionage 

Le LLM et l'interaction avec le LLM réduit les étapes de la correction au delà de son automatisation. Le LLM réécrit, il n'annote pas[^note], ne demande pas de clarifications ur les instructions données même si elles sont floues ('améliore le texte' est une instruction valide).

Un processus de suppression  qui est similaire aux logiques des éditeurs de texte WYSIWYG vs. le versionage qui rend compte du processus, entre dans une dimension de traçabilité et d'interprétabilité des choix effectués.

[^note]: on peut cependant prompter un modèle pour qu'il le fasse.

<!-- ici une illustration sur le versionage ? -->
 -->

# Langue, norme et normalisation politique 


# Histoire de la GEC 

## La correction d'erreur grammaticales automatique _Grammar Error correction_

Tâche de Traitement Automatique des Langues (TAL ou _Natural Language Processing_, NLP) voisine de la **traduction automatique** (TA ou _machine translation_, MT) 

Système expert : limité par des grammaires complexes, questions de pragmatique et d'idiomaticité.

Systèmes inductifs ou approches _data-driven_  :
D'abord des classifieurs pour prédire le mots le plus probable dans une classe (préposition), puis _statistical machine learning_ (SMT) dans les années 2010 et particulièrement _Neural machine translation_ (NMT). [@wangComprehensiveSurveyGrammar2020; @bryantGrammaticalErrorCorrection2023]

NMT : Correspondance entre des phrases ou portions de phrases en entrée et des portions de phrases attestées en grand nombre (seq2seq) à partir de corpus parallèle. Le modèle algorithmique est entraîné sur une paire de langue (ex : français->anglais). 


## Traduction automatique et LLMs

Un grand modèle de langue positionne chaque mot dans un espace vectoriel lors de sa phase d'apprentissage initiale à partir d'un grand volume de données en langue naturelle. 

Afin de donner une réponse le LLM (GPT, Mistral, Qwen, Llama etc.) situe la requête utilisateur dans son espace vectoriel et sélectionne les tokens les plus probables à partir du contexte donné (la requête utilisateur ou _prompt_ **et** les tokens qu'il a déjà généré). 

Les LLMs sont donc **généralistes**, ils ne sont pas destinés à la traduction plus qu'à la correction d'erreurs grammaticales ou à l'écriture créative.


## LLM vs NMT pour la Traduction automatique

<!-- si j'en parle c'est parce que la réflexion qui traverse le MT est la même que celle du GEC : vaut-il mieux un modèle qui fait plus d'erreurs mais qui sont prévisibles ou un modèle qui traduit mieux mais dont les fautes sont plus difficiles à cerner ? -->

<!-- Such divergences are well-documented in human translations (HT), where translators often make structural choices that vary significantly from the text originally written in the target language (Deng and Xue, 2017; Nikolaev et al., 2020). In contrast, traditional NMT outputs typically exhibit less diversity and more literal translations, lacking significant structural variation -->

NMT : traduction littérale , modèle spécialisé

LLM : traduction plus idiomatique, tendance à la confabulation. 

<!-- > « We find that while LLMs often exhibit translation patterns more similar to human translations compared to traditional NMT models, they still diverge from originally authored text in the same language. Overall, we find that automatically translated sentences from both NMTs and LLMs are consistently identified with higher accuracy in O/T classification tasks than human-translated ones »  -->

>« Furthermore, our frequency analysis of PoS tags reveals that LLMs align more closely with HT in their usage, especially in terms of adverbs, and auxiliary verbs, while NMT models tend to overproduce specific tags in shorter sentences. This suggests that LLMs, although not perfect, are making strides in mimicking human translation patterns. » [@sizovAnalysingTranslationArtifacts2024]

<!-- >« indicate that LLMs tend to produce translations that are less literal compared to NMT models »  -->

La fin de la NMT? 

>« What’s more, IBM announced the deprecation of Watson Language Translator, its NMT service, encouraging users to migrate to — guess what? — WatsonX LLMs. This move establishes IBM as one of the first tech giants to sunset its NMT efforts and focus on LLMs for automated translation purposes. » [@ciesielskiNeuralMachineTranslation2024]

## Le futur de la traduction automatique

>We anticipate that, soon, LLMs will become a viable enterprise solution for translation. This will likely come when we move towards task-specific LLMs trained specifically for translation. These models will be smaller and more practical to deploy and maintain than today’s massive foundational models. [@ciesielskiNeuralMachineTranslation2024]

Les LLMs font la traduction et l'évaluation de la traduction. 

## Question d'évaluation 

La traduction automatique : score BLEU (comparaison de la phrase traduite avec un référentiel de phrases bien traduites, score de proximité), WER (calcul du nombre de mot mal ou non traduit), METEOR etc. 

La Grammar Error Correction (GEC) compare la phrase source (avec erreurs), la phrase corrigée et une phrase de référence (la _ground truth_ donnée par un humain). Cette approche demande un corpus annoté en reference. 

## Métriques traditionnelles de GEC 

- Edit-Based Metrics :
    - M² (MaxMatch) : On aligne les phrases corrigées par le système avec celles de référence (gold standard), puis on extrait les "edits" (opérations de correction : insertion, suppression, remplacement). On calcule précision, rappel, F0.5(donc précision pondérée deux fois plus que rappel).
    - ERRANT (Error Annotation Toolkit): alignement de l'hypothèse avec la phrase source et la phrase cible et classification du type d'erreur (morphologie, orthographe, syntaxe). 
- Sentence-Based metrics:
    - GLEU (grammar-aware BLEU) : comparaison de n-grammes. 

Ces mesures repose sur l'alignement entre une hypothèse et une référence figée. 

## Mesure de la correction sans référence

Les métriques basées sur un corpus de référence limitent la correction a une forme seulement. 

Mesure sans référence [@napolesTheresNoComparison2016]: comparaison directe de la phrase source (avec erreurs) et de la phrase corrigée avec un LLM. 

Méthodes d'évaluation avec un LLM: 

- Proximité/distance : Comparaison des vecteurs de la phrase source et celles de la phrase corrigée. 
- Perplexité/log-probabilité : plus une phrase est fluide plus elle est probable (donc correcte). 
<!-- log-probabilité : probabilité d'une phrase dans un modèle, le logarithme est utilisé car les proba sont très faibles
perplexité : inverse de la probabilité moyenne par mot, basse perplexité = LM trouve la phrase prévisible, fluide, naturelle. comparaison des scores de perplexité sur source puis hypothèse -->
- Spécialisation d'un LLM pour l'évaluation : _Machine learning_ sur un corpus annoté avec des scores attribué ex: SOME [@yoshimuraReferencelessSubMetricsOptimized2020]
- LLM as judges : instruction en langues naturelles.

> « The decrease in correlation as the LLM scale decreases, such as with Llama 2 and GPT-3.5, suggests the importance of the LLM scale. Especially, the decrease in correlation when adding fluent corrected sentences (“+ Fluent corr.”) compared to “Base” implies that smaller-scale LLMs may not adequately consider the fluency of sentences. Possible reasons for this include issues such as LLM’s tendency to produce the same scores (Appendix C) and the inability to interpret the context of prompts as expected by users. However, GPT-4 consistently demonstrated a high correlation and provided more stable evaluations compared to traditional metrics. » [@kobayashiLargeLanguageModels2024]


## Les limites des LLMs-as-judge pour la GEC

- Pas toujours reproductible
- Favorise les langues bien dotées. Ex Bengali [@maityHowReadyAre2024]
- @shankarWhoValidatesValidators2024a et le _criteria drift_ : on ne sait pas avant de l'avoir expérimenté ce que le LLM est capable de faire correctement.  Autrement dit : l'évaluation est un processus itératif. 

<!-- on entre dans une boucle où en pensant déléguer à un LLM la tâche de correction, on se retrouve à devoir itérativement penser la correction et l'évaluation proposée : finalement est-ce que notre capacité de correction n'est déplacée sur un nouvel outil mais toujours aussi nécessaire.  -->

# Enjeux et conséquences

## Est-ce que ces outils offrent un gain de temps selon vous ?

## Uniformisation de la langue 

model collapse 

linguistic uniformisation


## L'alignement des valeurs et le système de valeurs

>« The problem of achieving agreement between our true preferences and the objective we put into the machine is called the value alignment problem: the values or objectives put into Value alignment problem the machine must be aligned with those of the human. » [@russellArtificialIntelligenceModern2022a, p. 23]

L'intelligence humaine commence là où celle de la machine s'arrête. Si on découvre de nouvelles capacités à la machine alors on enlève cette capicité de la définition de l'intelligence humaine. « More than fifteen years ago Hilary Putnam identified the old problem we face to this day: ‘The question that won’t go away is how much what we call intelligence presupposes the rest of human nature’ (1988: LET} » [@mccartyHumanitiesComputing2005, p. 41]


Autrement dit, si on laisse à la machine cette tâche c'est qu'on tend à l'estimer comme peu valorisante dans notre système de valeur actuel. Quelles conséquences est-ce que déléguer cette partie du travail a sur notre travail ? 

## Des 'petites' corrections finales ?

>Currently, academic publishers only allow the use of ChatGPT and similar tools to improve the readability and language of research articles. However, the ethical boundaries and acceptable usage of AI in academic writing are still undefined, and neither humans nor AI detection tools can reliably identify text generated by AI [@homolakExploringAdoptionChatGPT2023]

<!-- pas de définition claire de la correction sur le plan académique = pas de limite non plus. 
Est-ce que refaire une table en utilisant un LLM càd en prenant le risque qu'il hallucine sur des données demande un usage cité de ChatGPT ? 
Si le contenu dépend du style, est-ce que la réécriture ne modifie pas le contenu original intellectuel ? 
Est-ce que faire un état de l'art (càd pas de production de nouveau contenu) avec chatGPT n'influence pas le travail de recherche ?  -->

>It is being increasingly observed that content generated by ChatGPT is going undeclared and undetected, resulting in its appearance in articles published in scholarly journals. 
[...] The general policy among publishers states that AI tools must not be used to create, alter or manipulate original research data and results (Elsevier., 2023; Roche, 2024).[@strzeleckiMyLastKnowledge2025]

![Articles contenant des réponses de prompts](img/chatgptresponses.png)

![Articles contenant des réponses explicites de ChatGPT](img/chatgptresponses2.png)

<!-- ici l'argumentaire c'est que comme on a laissé à ChatGPT la taĉhe de rédaction et possiblement de relecture finale on s'embête pas à relire la version de l'article soumise, donc on laisse des dingueries.  -->
<!-- 
## Quelle conséquence concrétement ?

deux points de vue : 
- La correction a un impact sur la manière dont le texte est reçu. Le pdv des outils : peaufiner pour 'convey at best' tes idées, respecter les idées de l'auteurice.
- "Écrire c'est réécrire." donc laisser la correction à la machine c'est laisser une partie importante du travail intellectuel. 
    - surtout si on considère les pratiques réelles où l'écriture est faite d'itération avec des étapes de corrections et des relectures. 
    - ce qui était rationalisé dans le monde de l'imprimé avec le système ddes 'épreuves' à al soumission d'un manuscrit. 

À quel moment est-ce que cette étape intervient ? Et quelle est la conséquence d'automatiser cette étape ? 

- au cours de la rédaction ? 
    - évanouissement des versions intermédiaires (suppression vs. versioning) ?
- à la fin de la rédaction ?  -->

## Effet nivelant et influence de la machine


Les moins bons traducteurs sont aidés par la TA mais les meilleurs traducteurs sont désavantagés par la TA. Effet limitant car tendance à se laisser influencer : réduction des intuitions de traduction et de la créativité traductionnelle.[@schumacherPosteditionTraductionAutomatique2023]

Une influence pas négligeable : même quand un participant n'a plus les recommandations de la machine, iel reproduit les erreurs des recommandations [@vicenteHumansInheritArtificial2023] : délégation cognitive ou _cognitive offloading_ 


<!-- 1. intégrer la question du correcteur automatique intégré dans le téléphone ? iirc le discours était que le correcteur automatique rendait flemmard, ajd il faut souvent lutter contre son téléphone pour dire des choses correctes -->

# Quelques outils


## Outils généralistes

LLMs non spécialisé : ChatGPT, modèles téléchargés localement (ollama), Mistral, Llama, Claude etc.

Il faut tenir compte des biais du modèle et du _prompt_ : interprétation. 

## L'effet 'AI-powered'

La correction automatique existe avant ChatGPT et les LLM offraient des techniques poussées de GEC mais il fallait encore que de **nouveaux usages s'ancrent** et qu'il y ait un **intérêt économique à maintenir l'utilisateur sur la même plateforme** d'où l'intégration de LLM dans l'outil. 

## Outils spécialisés 


### Les outils historiques (francophones)

**[Antidote](https://www.antidote.info)**

Sources sur les technologies d'Antidotes  :

[Reformulation et IA (décembre 2023)](https://www.antidote.info/fr/blogue/nouvelles/reformulation-et-intelligence-artificielle-antidote
)

[ChatGPT peut-il remplacer Antidote ?](août 2025)(https://www.antidote.info/fr/blogue/astuces-et-conseils/chatgpt-peutil-remplacer-antidote)

Une combinaison d'outils spécialisés et utilisant des techniques diverses. 

**[ProLexis](https://www.prolexis.com/)** (pas de vidéos youtube depuis 3 ans, ProLexis7) Outil professionel, analyseur syntaxique, interface à l'ancienne, [powerpoint à l'ancienne](https://www.youtube.com/watch?v=xTxBdv-zpIY).


### Les nouveaux outils

[EditPad](https://www.editpad.org/) : AI detector, humanize AI text, Plagiarim checker, paraphrasing tool, story generator, text summarizer, AI essay writer etc. Probablement juste ChatGPT hooked à une interface avec un system-prompt. Apparamment mauvais according to @bordalejoScarletCloakForest2025

![screenshot editpad](img/editpad.png) 

Corriger = masquer que le texte ne vient pas d'une machine, ou chercher à le détecter?

[Writefull](https://www.writefull.com/): Title generator, Abstract generator, paraphraser, academizer.

Effet de mode = disparition et apparition de solutions miracles (down le 22 septembre, up le 30 septembre mais bug)

[Grammarly](https://www.grammarly.com/) donne une note à partir des critères de formalité, 4 niveaux : correctness (corrige erreurs grammaticales), clarity (reformulation) engagement (option payante), delivery (payant), plagiarism detection (payant). Option 'generative AI' avec des prompts pre-écrits qui restreignent l'usage. Et un browser plugin qui permet de s'en servir avec tous les sites google (docs, gmail, youtube comments). 

_improve_ est une option liée à "Generative AI" juste 'améliorer'. 

<!-- "Grammarly is the AI communication partner trusted by over 40 million people, 50,000 organizations, and people at 96% of the Fortune 500." -->

[quillbot](https://quillbot.com/)

>"Is QuillBot considered AI writing?
>2 years ago Updated 
>Everyone’s talking about AI writing these days, and debate over its use — and misuse — rages. QuillBot has helped you grow and improve as a writer, but you may wonder if using it is considered AI writing. Good question. **The short answer is “no.” QuillBot’s tools have specific uses, such as correcting grammar or paraphrasing sentences. It’s up to you to use the feedback and suggestions to create content that is solely your own.** ChatGPT and similar AI writers, on the other hand, can generate essay-length text from a few prompts. That writing can then be presented with no changes. Since QuillBot is not considered AI writing, most plagiarism checkers will not flag its use.

>That said, we make no guarantees if someone uses QuillBot on text generated by a tool like ChatGPT. Why not play it safe and craft the content yourself? (With QuillBot’s help, of course!)



## Tous les autres outils 

Prise de note :

[Notion](https://www.notion.com/) : génération de texte. 

[Evernote](https://evernote.com/fr-fr): RAG 

Rédaction de mail etc




## Bibliographie

