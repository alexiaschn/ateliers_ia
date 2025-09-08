---
# layout: slide
title: Intro 
date: 2025-09-11
author: Alexia Schneider `alexia.schneider@umontreal.ca` (UdeM), 
  Marcello Vitali-Rosati `marcello.vitali.rosati@umontreal.ca` (UdeM)
bibliography: ../phd_udem.bib
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

Théorie : 

1. Présentation de la série d'atelier 
2. Qu'est-ce que l'IA ? 
3. Intérêt d'étudier l'IA pour les SHS
4. Retours historiques
5. Typologie des IA
6. Cas d'usage et modélisation experte (ELIZA)
7. Principe fondamentaux de l'apprentissage machine (modèles spécialisés)
8. Les LLMs : les modèles généralistes

Pratique : 

1. visualisation et manipulation d'une approche experte
2. visualisation du principe de vectorisation
3. Paramètres de chatbots (duck.ai)
4. Interprétabilité des chatbots (Neuronpédia)
5. Prompt Engineering (ChainForge)
6. Intégration de chatbot localement (Ollama)


## Présentation et objectif des ateliers 

Format : 4 séances de 2heures, sans inscription, participation libre (à justifier pour le certificat des Humanités Numériques)

Théorie et pratique en alternance au cours des deux heures.

Objectifs de la série d'atelier : 

- Comprendre les fondamentaux de l'IA et son histoire
- Obtenir des notions critiques sur le fonctionnement profond des outils
- Tester et s'approprier des outils d'IA 
- Maîtriser le vocabulaire de la discipline

Objectifs de cet atelier : 

- Comprendre les différentes formes d'IA
- Comprendre les enjeux liés à l'utilisation des LLM
- Tester différents paramètres d'IA générative.
- Installer localement des modèles de langue.

## Certificat canadien en Humanités Numériques

![Certificat canadien en HN](/seances/img/ccdhn1.png)

![Certificat canadien en HN](/seances/img/ccdhn2.png)
![Certificat canadien en HN](/seances/img/ccdhn3.png)

[Information sur le certificat](https://ccdhhn.ca/)

## Qu'est ce que l'IA ? 

- Tout et rien : exemples : chatbot, détection sur des imageries médicales, HTR, DeepBlue. 

- le dernier mot à la mode. Le 'numérique' des années 2020. [@vitali-rosatiManifestePourEtudes2025]. 

Définition pratique : "un programme informatique qui effectue une prédiction." 


~~À quoi sert d'étudier l'IA pour les chercheur.se.s en SHS~~

## L'IA et les SHS

Que peuvent faire les SHS pour l'IA ? 

- participer à la réflexion actuelle sur son utilisation : 
    - positionnements de revues et de conférences (pose un cadre, parfois un précédent)
- proposer une théorie critique de l'IA décentrées de l'effet 'benchmarking' (i.e. comparaison des modèles ou des entreprises qui les mettent à disposition)
- proposer une avis sur l'utilisation de ces outils qui soit propre à sa discipline (ex: distinguer des usages en fonction des besoins particuliers de son domaine). 


## Exemples de prises de position 

>Both SUP and JHUP have increasingly embraced, tested, and deployed some AI tools and policies. Barbara has been clear in her support of responsible uses of AI and the necessity of leveraging these early days to stake a claim within the quickly evolving landscape. Like SUP, JHUP is building and testing its own tools for marketing, accessibility, and analytics, efforts which place our presses in a position to potentially build services that might in the future even benefit other university presses. [@mulliken2025AUPressesWeekinResidence2025]

>we offer recommendations for citing generative AI, defined as a tool that “can analyze or summarize content from a huge set of information, including web pages, books and other writing available on the internet, and use that data to create original new content” (Weed). [@HowCiteGenerative2023]

> The uncomfortable truth for researchers and publishers who oppose AI slowly taking over human review is that they might not be able to prevent it. Should a researcher use AI to write the first pass of peer review and not disclose it — in contravention of publisher guidelines — that might not be detectable, says Hosseini, who is also one of the editors of the journal Accountability in Research. And if AI reviews become widespread, that could change the practice of science, says Priem. “Every researcher can run their own bespoke review service over the preprint/dataset landscape, flagging/extracting only the science they care about (at any “quality” level) they want that day,” he wrote on X earlier this year. That could start to eat into the roles of journals, by taking away the certification that peer review mediated by journals provides, he says.
[@naddafAITransformingPeer2025]

> Building critical AI literacies is a process of  empowerment that enables students and citizens to exercise independent judgment about whether or if to  use this very new and largely untested commercial technology. [@criticalai@rutgersCriticalAILiteracies2024]


## Brève histoire de l'IA (pt. 1)

(1940s : Science-fiction et roman d'Isaac Asimov _Runaround_ en 1942.)

[@turingComputingMachineryIntelligence1950] : 'can machines think?'

1956: 'intelligence artificielle', Minsky et McCarthy à la Dartmouth Summer Research Project on Artificial Intelligence (DSRPAI). 

1966 : ELIZA [@weizenbaumELIZAComputerProgram1966]

1990-2000s : pic des systèmes experts et des arbres de décision. DeepBlue d'IBM [@campbellDeepBlue2002]. 


## Brève histoire de l'IA (pt. 2)

2010s : pic des systèmes d'IA avec une modélisation distributionnelle du language (vecteur). Word2Vec [@mikolovEfficientEstimationWord2013], GloVE [@penningtonGloVeGlobalVectors2014]. Parmi les avancées majeures de cette modélisation on compte le mécanisme d'attention [@vaswaniAttentionAllYou2017] et l'encodage bidirectionnel BERT [@devlinBERTPretrainingDeep2019] qui permettent des modèles très performants comme le GPT-3 d'OpenAI [@brownLanguageModelsAre2020]. 

Actuellement : tendance à l'hybridation de ces modèles : Neuro-Symbolic Integration, Semantic Web Machine Learning [@marcusNextDecadeAI2020], {{< cite "kautzThirdAISummer2022">}}, 
[@russellArtificialIntelligenceModern2022]

## Typologie de l'IA

- Approche experte ou modèle symbolique : modélisation d'un programme à partir de **règles** précises. Les règles doivent être applicables à de nouvelles données pour faire une prédiction.

- Approche inductive ou modèle d'apprentissage machine (_machine learning_) : modélisation d'un programme à partir d'un grand volume de données. Ce sont les **motifs de répétitions** qui permettent à la machine d'émettre une prédiction. 

## Ce qu'il faut retenir

- L'IA réfère à plusieurs type de modélisations pour la prédiction : une approche déductive et une approche inductive. 
- On parle 'des saisons' de l'IA pour évoquer l'attrait public de la discipline et son avancée depuis les années 1950. 
- Par conséquent, certaines approches attirent l'attention à un moment donné, actuellement IA = chatbot voire ChatGPT. 
- L'IA réfère à des algorithmes qui permettent d'automatiser une prise de décision et pas seulement à des programmes de génération textuelle. 

## Partons d'un exemple 

Objectif : obtenir un programme capable de classer une phrase selon une thématique prédéfinie. 

Exemple : Classification d'un texte soit en "parle de fruit" soit en "ne parle pas de fruit". 

## Modéliser une approche experte 

- faire appel à un expert : un humain pour déterminer les règles qui définissent ce qui est une phrase parlant de fruits. 
- exemple de règle possible : liste de mots comme 'pomme, pommes, banane, poire etc.' ordre des mots ou POS pour distinguer 'orange' couleur du fruit par exemple. 

Une approche qui sembler simpliste en apparence mais qui : 

- peut s'avérer très complexe (ex: traduction)
- est la base de systèmes très performants 
- entre dans une logique de _lazy computing_ [@fujinagaVirtuesLazyMachines2025]
- révèle les tâches de bas niveau pour passer d'une chaîne de caractères à un ensemble de caractéristiques : tokenisation, POS-tagging. 

[Programme de démo](https://demo-atelier.streamlit.app/)

## Exemple d'un programme conversationnel /génération textuelle avec une approche experte ELIZA

Try it yourself : [ELIZA](https://anthay.github.io/eliza.html)

>Eliza is a pattern-matching automated psychiatrist. Given a set of rules in the form of input/output patterns, Eliza will attempt to recognize user input phrases and generate relevant psychobabble responses. Each rule is specified by an input pattern and a list of output patterns. A pattern is a sentence consisting of space-separated words and variables. [@connellyElizapy]  


Exemple de _literate programming_ [@knuthLiterateProgramming1984] : 

[Lire le code d'ELIZA](https://dhconnelly.com/paip-python/docs/paip/eliza.html)


## Approche inductive : le machine learning classique

### 1e étape Modélisation des données

- **Constitution d'un corpus** : obtenir un ensemble important de documents 
- **Annotation** : attribution d'une classe à chaque document par un humain/expert, _ground truth_ ou vérité de terrain. 
- **Encodage vectoriel** : Comptage des tokens dans l'ensemble du jeu de données et dans chaque phrase/document. 
- On obtient une représentation vectorielle = coordonnées dans un espace vectoriel à _n_ dimensions.


### 2e étape Choix de l'algorithme de classification

Différentes logiques permettent de distinguer les données entre elles. Quelques exemples d'apprentissage machine classique : 

- K-Nearest Neighbor -> le token apartient à la même classe que ses voisins (au nombre K)
- Arbre de décision -> on construit un arbre de questions fermées qui dessine le jeu de données.
- Regression logistique -> une ligne sépare l'espace vectoriel entre les deux classes


### 3e étape Entraînement supervisé : apprentissage spécialisé 

**Ajustement des poids** (valeurs des vecteurs) à partir de données spécialisées

[Programme de démo](https://demo-atelier.streamlit.app/)


## Approche inductive généraliste : les LLMs 

Exemple de LLMs : BERT, GPT-4, Mixtral, Gemini, Llama, Qwen, DeepSeek etc. 

### Foundational models : Pré-entrainement

**Constitution d'un corpus non annoté**

**Apprentissage auto-supervisé** : le modèle apprend à prédire le mot suivant ou remplir un blanc dans une phrase.

**Encodage itératif** : chaque mot/token est encodé en vecteur (embeddings) et le réseau ajuste ses poids en fonction du contexte.

Dès cette étape on obtient un modèle généraliste capable de faire des prédictions à partir d'une requête en langue naturelle. 

### Fine-tuning affinage.

Spécialisation du modèle sur une tâche précise à partir d'un jeu de données annotées.

### Alignement

**Instruction-tuning** : entraînement supervisé sur des données "question → réponse".

**Reinforcement Learning with Human Feedback** : des annotateurs évaluent les sorties du modèle, et un apprentissage par renforcement ajuste les préférences du modèle.

## En résumé 

Modèle de langue = modélisation de la langue dans son ensemble + capacité de prédiction. 

Les LLMs font de la prédiction de token : 

- la génération de texte n'est pas la première ni la seule utilisation des LLMs. 
- soliciter un LLM pour générer un texte demande de recalculer le token le plus probable à chaque token -> coût énergétique important. 


## LLMs et chatbot

Parce que les LLMs sont lourds (plusieurs Gigas) et parce qu'il est coûteux en énergie d'effectuer les calculs qui permettent de déterminer le prochain token (plusieurs GPU), l'usage le plus courant des IA générative est via le site propriétaire qui va interroger le modèle sur un serveur distant. C'est la forme ChatGPT, Mistral.ai, etc. 


## Duck.ai

[duck.ai](https://duck.ai) permet de comparer des modèles en interfaces chat tout en conservant des données privées. 

## _Circuit Tracing_

Interprétation du méchanisme par lequel un modèle effectue produit une prédiction à partir d'un prompt. 

[Neuronpedia 'circuit tracing' demo](https://www.neuronpedia.org/gemma-2-2b/graph?slug=gemma-basket&pruningThreshold=0.6&densityThreshold=1) : Explication du processus interne d'un LLM pour la prédiction d'un token à partir d'un prompt.

[@ameisenCircuitTracingRevealing2025]

## Ollama

Il est possible de faire tourner un SLM (small language model) localement. Pour ce faire : `ollama` est une bibliothèque qui permet de télécharger et d'utiliser localement un LLMs. 


### Installation et utilisation de Ollama 

[Téléchargement de Ollama](https://ollama.com/download)

### Utilisation de Ollama en invite de commande


```ollama run llama3.2``` -> télécharge et lance le modèle.

""" -> pour des instructions longues

`/show info` -> information sur le modèle téléchargé

`ollama list` -> liste des modèles téléchargés et utilisables


`ollama rm llama3.2` -> supprime un modèle 


## Paramètres d'un modèle 

- Le **seed** (nombre que l'on peut choisir): les LLMs ont une variable aléatoire au moment de l'encodage des données et au moment du requêtage : le seed permet d'utiliser toujours le même ordre aléatoire, càd d'obtenir pour un même prompt toujours la même réponse. Enjeu de reproductibilité. 
- La **température** (valeur de 0 à 1): détermine le degré d'utilisation de la variable aléatoire. Une température élevée signifie que le modèle sera plus "créatif" car il donnera plus probablement un token qui a une probabilité absolue moindre dans son contexte.
- **top_k** (valeur de 0 à 100): variable qui réduit la probabilité de générer des tokens absurdes. Une valeur élevée donne des réponses plus variées et une valeur basse des réponses plus conservatrices. (Défaut 40)
- **top_p** (valeur de 0 à 1): Fonctionne avec le top_k. Une valeur haute donne un texte varié, une valeur basse, un texte conservateur. (Défaut: 0,9)

Source : [Documentation Ollama](https://github.com/ollama/ollama/blob/main/docs/modelfile.md#parameter)

## Model Steering ou System message

Reconduire un modèle consiste à lui fournir des ordres qui vont modifier son comportement pour toutes les interactions suivantes : cette instruction initiale est le "System message". 

[Steer model interactively on Neuronpedia](https://www.neuronpedia.org/gemma-2-9b-it/steer)

[Tutoriel](https://github.com/ollama/ollama/blob/main/docs/modelfile.md)

Créer un nouveau document 'Modelfile' sans extension. 

Linux : `cat > Modelfile` puis CTRL+C : 

>FROM llama3.2
PARAMETER temperature 1
top_k 100
top_p 1
seed 17
SYSTEM "Tu es un chien"

puis CTRL+SHIFT+D et CTRL+D


Windows cmd (Win+R):  ```echo 'FROM llama3.2
PARAMETER temperature 1
top_k 100
top_p 1
seed 17
SYSTEM "Tu es un chien"' > Modelfile``` (CTRL+SHIFT+D)


Ou c/c manuellement : 

>FROM llama3.2
PARAMETER temperature 1
top_k 100
top_p 1
seed 17
SYSTEM "Tu es un chien"

```ollama create chien -f Modelfile```

```ollama run chien```


## Limites des interfaces de chat 

'hacker un LLM' avec du _prompt injection_ ou autres techniques de _jailbreaking_. 

[Incitent database](https://incidentdatabase.ai/) 

>Hidden prompts reportedly were discovered in at least 17 academic preprints on arXiv that purportedly instructed AI tools to deliver only positive peer reviews. The lead authors are reportedly affiliated with 14 institutions in eight countries, including Waseda University, KAIST, Peking University, and the University of Washington. The alleged concealed instructions, some of which were reportedly embedded using white text or tiny fonts, were purportedly intended to influence any reviewers who rely on AI tools. (https://incidentdatabase.ai/cite/1135)


Les hallucinations : **il n'y a pas d'hallucinations**, toutes les générations produites par un LLMs ont la même teneur de vérité du point de vue de l'outil : le modèle ne peut pas évaluer sa réponse à l'aune d'un référentiel extérieur. 

## Le prompt engineering

Rendre un prompt robuste et surtout permettre l'évaluation systématique d'une stratégie de prompt. Réintégrer une forme de modélisation de son problème pour optimiser un prompt : le template. 

[ChainForge](https://chainforge.ai/play/) : outil de comparaison de prompt : comparaison de modèle, comparaison de template (un texte qui inclut des variables) visualisation côte à côte des sorties. 


## Études critiques de l'IA

Discipline émergente : [Critical AI revue](https://read.dukeupress.edu/critical-ai/issue/3/1) lancée en 2023.

Pistes de réflexions : 

- Uniformisation des pratiques et des modes de pensées : l'interface de chat est une façon de formaliser son problème, quid de la recherche de solution en interrogeant des moteurs de recherche, des bases de données ou des archives spécialisées ? 
- Derrière l'apparente accessibilité de l'interface de chat, est-ce qu'on ne risque pas de creuser l'écart de la littératie numérique ? 
- Est-ce que ces connaissances spécifiques, comme celles du code, qui impliquent des capacités de raisonnement alternatives, ne risquent pas de se retrouver suelement dans une forme d'élite intellectuelle ? 
- Comment peut-on définir une littéracie propre aux outils d'IA ? 
- Quelle posture adopter ? Faut-il interdire l'usage dans la recherche ou l'enseignement, obliger une déclaration d'utilisation/citation ou encore laisser faire selon les usages et opter pour une approche pédagogique ?

## Ce qu'il faut retenir

- L'IA est amalgamé aux LLMs et en particulier aux interfaces de chatbots mais cela recouvre en réalité des processus algorithmiques variés.
- L'histoire de l'IA a montré qu'il y a des phases tant dans les approches valorisées que dans l'approbation de l''intelligence artificielle' opposée à l'intelligence humaine.
- un système expert (symbolique) peut être aussi complexe et 'intelligent' qu'un LLM.
- Les systèmes d'IA n'ont pas de connaissance du réel et sont des modèles purement probabilistes. 
- Les 'halllucinations' ne sont pas des anomalies, ce sont des erreurs que l'on qualifie a postériori comme telles. 
- Les systèmes inductifs sont appropriés pour certaines tâches : classification, production de résumé. Leur point fort reste leur adaptabilité à de nouveaux contextes. 
- Les chatbots sont des interfaces qui permettent un échange homme-machine en langue naturelle : l'exploitation des capacités inductives d'un LLMs ne nécessite pas de passer par une telle interface. Ex : classification, processus expérimental plus adapté à une utilisation sans cette interface. 

## Ressources vues pendant l'atelier

[Démo IA symbolique/IA connexioniste pour les ateliers](https://demo-atelier.streamlit.app/)

[Duck.ai](https://duck.ai) : Comparaison de modèles sous forme de chatbot et paramétrage. 

[ChainForge](https://chainforge.ai/play/) : comparaison de prompts 


[Ollama](https://ollama.com/download) et [documentation](https://github.com/ollama/ollama/blob/main/docs/modelfile.md) : Téléchargement de LLM localement. Possibilité de _steer_ un modèle.

[Neuronpedia 'steer' demo](https://www.neuronpedia.org/gemma-2-9b-it/steer) : Comparaison d'un modèle qui a été 'redirigé' ou non.

[Neuronpedia 'circuit tracing' demo](https://www.neuronpedia.org/gemma-2-2b/graph?slug=gemma-basket&pruningThreshold=0.6&densityThreshold=1) : Explication du processus interne d'un LLM pour la prédiction d'un token à partir d'un prompt.

[Incident Database AI](https://incidentdatabase.ai/) : Résumé des incidents et controverses relevées dans la presse lié aux IA (en anglais).

[Critical AI journal](https://read.dukeupress.edu/critical-ai) : Revue

<!-- ## Annexe : glossaire


**document** : ici une phrase

**classes** : ensemble thématique de la classification. Ex : "fruit" et "non fruit" pour la classification binaire de notre exemple. 

**jeu de données** : ensemble des documents 

**apprentissage supervisé** : méthode d'apprentissage machine à partir de classes connues.

**apprentissage non-supervisé** : méthode d'apprentissage machine sans connaître les classes à l'avance : a pour objectif de déterminer les caractéristiques discriminantes d'un jeu de données.

**vérité de terrain** ou _ground truth_ : annotation effectuée par un humain sur l'ensemble du jeu de données.  -->


## Bibliographie

<!-- 
## Bibliographie
 
Ameisen, AUTHORS Emmanuel, Jack Lindsey, Adam Pearce, Wes Gurnee, Nicholas L. Turner, Brian Chen, Craig Citro, et al. 2025. “Circuit Tracing: Revealing Computational Graphs in Language Models.” Transformer Circuits. https://transformer-circuits.pub/2025/attribution-graphs/methods.html.

Breit, Anna, Laura Waltersdorfer, Fajar J. Ekaputra, Marta Sabou, Andreas Ekelhart, Andreea Iana, Heiko Paulheim, et al. 2023. “Combining Machine Learning and Semantic Web: A Systematic Mapping Study.” ACM Computing Surveys 55 (14s): 313:1–41. https://doi.org/10.1145/3586163.

Brown, Tom B., Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, et al. 2020. “Language Models Are Few-Shot Learners.” arXiv. https://doi.org/10.48550/arXiv.2005.14165.

Campbell, Murray, A. Joseph Hoane, and Feng-hsiung Hsu. 2002. “Deep Blue.” Artificial Intelligence 134 (1): 57–83. https://doi.org/10.1016/S0004-3702(01)00129-1.
Connelly, Daniel. n.d. “Eliza.py.” Eliza Emulation Python. https://dhconnelly.com/paip-python/docs/paip/eliza.html. Accessed August 20, 2025.

Devlin, Jacob, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2019. “BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.” In Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers), edited by Jill Burstein, Christy Doran, and Thamar Solorio, 4171–86. Minneapolis, Minnesota: Association for Computational Linguistics. https://doi.org/10.18653/v1/N19-1423.

Fujinaga, Ichiro. 2025. “On the virtues of lazy machines.” {Keynote}. Montréal.

Haenlein, Michael, and Andreas Kaplan. 2019. “A Brief History of Artificial Intelligence: On the Past, Present, and Future of Artificial Intelligence.” California Management Review 61 (4): 5–14. https://doi.org/10.1177/0008125619864925.

“How Do I Cite Generative AI in MLA Style?” 2023. MLA Style Center.

Knuth, D. E. 1984. “Literate Programming.” The Computer Journal 27 (2): 97–111. https://doi.org/10.1093/comjnl/27.2.97.

Marcus, Gary. 2020. “The Next Decade in AI: Four Steps Towards Robust Artificial Intelligence.” arXiv. https://doi.org/10.48550/arXiv.2002.06177.

Mikolov, Tomas, Kai Chen, Greg Corrado, and Jeffrey Dean. 2013. “Efficient Estimation of Word Representations in Vector Space.” arXiv. https://doi.org/10.48550/arXiv.1301.3781.

Mulliken, Jasmine. 2025. “2025 AUPresses Week-in-Residence Report.”

Naddaf, Miryam. 2025. “AI Is Transforming Peer Review — and Many Scientists Are Worried.” Nature 639 (8056): 852–54. https://doi.org/10.1038/d41586-025-00894-7.

Pennington, Jeffrey, Richard Socher, and Christopher Manning. 2014. “GloVe: Global Vectors for Word Representation.” In Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP), edited by Alessandro Moschitti, Bo Pang, and Walter Daelemans, 1532–43. Doha, Qatar: Association for Computational Linguistics. https://doi.org/10.3115/v1/D14-1162.

Turing, A. M. 1950. “Computing Machinery and Intelligence.” Mind LIX (236): 433–60. https://doi.org/10.1093/mind/LIX.236.433.

Vaswani, Ashish, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin. 2017. “Attention Is All You Need.” arXiv. https://doi.org/10.48550/arXiv.1706.03762.

Vitali-Rosati, Marcello. 2025. “Manifeste Pour Des Études Critiques de l’Intelligence Artificielle.” Culture Numérique. Pour Une Philosophie Du Numérique.

Weizenbaum, Joseph. 1966. “ELIZA—a Computer Program for the Study of Natural Language Communication Between Man and Machine.” Communications of the ACM 9 (1): 36–45. https://doi.org/10.1145/365153.365168. -->

<!-- Baliser les diapositives avec les shortcodes `{{< psectioni >}}` pour ouvrir et `{{< psectiono >}}` pour fermer. -->

<!-- 

{{< psectioni >}}

{{< psectiono >}} -->

