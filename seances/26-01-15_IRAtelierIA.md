---
title: Atelier IA - Recherche d'information et synthèse des sources 
author: Alexia Schneider 
date: 15 janvier 2026
place: BLSH
bibliography: ../phd_udem.bib
link-citations: true
colorlinks: true
fig-cap-location: bottom
logo: "stickerAvecTexte.png"
format:
    revealjs: 
        output-file: "ri.html" 
        # template: simple
        smaller: true
        # incremental: true
        scrollable: true
        slide-number: true
---

## Programme de la séance 

<!-- ouvrir splat1.html, 
ouvrir le splat1  à combinedScore pour changer poids de la recherche hybride
ouvrir splat1 à  tools pour montrer les fonctions  -->

1. Introduction et rappels
2. Les systèmes complexes intégrant de l'IA: les agents IA
3. le RAG
4. RAG et applications généralistes
5. Les Assistants de recherche 'AI powered'

## Présentation et objectif des ateliers 

Format : 4 séances de 2heures, sans inscription, participation libre (à justifier pour le certificat des Humanités Numériques)

Objectifs de la série d'atelier : 

- Comprendre les fondamentaux de l'IA et de son histoire
- Obtenir des notions critiques sur le fonctionnement profond des outils
- Cerner les enjeux actuels sur des thématiques qui affectent la recherche et l'enseignement


## Certificat canadien en Humanités Numériques

![Certificat canadien en HN](/seances/img/ccdhn1.png)

![Certificat canadien en HN](/seances/img/ccdhn2.png)
![Certificat canadien en HN](/seances/img/ccdhn3.png)

[Information sur le certificat](https://ccdhhn.ca/)

# Les fondamentaux : rappels 

## Qu'est ce que l'IA ? 
 
Des programmes informatiques que nous estimons à la hauteur de l'intelligence humaine ? Le développement des technologies fait évoluer cette définition de l'_intelligence_ non seulement _artificielle_ mais aussi _humaine_.

'IA' depuis 5 ans, a remplacé le 'numérique' des années 2010, et le 'cyberespace' des années 1990 et 2000.[@vitali-rosatiManifestePourEtudes2025a]. 

Définition pratique pour ces ateliers: "un programme informatique qui effectue une prédiction."

## Rappels : histoire de la discipline

- L'IA n'est pas une nouvelle discipline (terme de 1956 lors de la Dartmouth Summer Research Project on Artificial Intelligence par Marvin Minsky et John McCarthy). 
- L'article _Computing Machinery and Intelligence_ de @turingComputingMachineryIntelligence1950 a orienté la discipline vers la création de chatbots.
- Les 'saisons de l'IA' suivent des phases d'approbation publique et de désintérêt pour le terme et les technologies associées.
- Changement de paradigmes actuels : de l'outil qui assiste à l'outil qui produit à l'outil qui trompe (correction orthotypo -> reformulation -> génération -> masquage de son utilisation). 
- Ce qu'on fait entrer dans la catégorie d'"intelligent" a changé : le calcul savant est-il moins intelligent que le bavardage ? 

## Rappels : IA symbolique / IA connexionniste

- Deux grandes approches en IA : une approche déductive (IA symbolique, système expert) vs. approche inductive (IA connexionniste, modèle de langue basé sur des plongements de mots ou _embeddings_ = vecteurs). 
- Un LLM (_large language model_) est la modélisation sous forme de vecteurs de chaque élément d'un très grand corpus (_token_ ~mot) par rapport à cet ensemble. 
- Un système expert peut être aussi complexe et énergivore qu'un LLM.

![Plongements lexicaux ou _word embeddings_](img/word_embedding.png)

![Comparaison de vecteurs dans un espace à deux dimensions](img/vecteurs.png)

![Classification avec algorithme K-Nearest-Neighbor d'une troisième phrase ](img/comparaisonKNN.png)

## Rappel sur les LLMs 

- Chatbots type ChatGPT, Mistral, Gemini, Claude etc. = application qui utilise un LLM (la représentation figée de la langue en vecteurs) pour faire de la prédiction de tokens (génération).  
- Absence de référent ou de règle : probabilité pure -> plausible et convaincant.
- Les hallucinations =/= anomalies 
- Les outils reflètent les intérêts et la vision du monde de ceux qui les concoivent: correcteurs orthographiques et grammaticaux incarnent une vision du monde centrée sur la productivité et la rapidité.
- Exploitation des capacités inductives d'un LLM ne dépend pas d'une interface en langue naturelle. Ex : classification avec de l'apprentissage machine (_machine learning_). 

# Des systèmes d'IA complexes

## Quelle complexité ?

IA, dite générative ou d'automatisation de la prédiction de token, effectue aujourd'hui des tâches complexes à deux niveaux: 

- interprétation d'une instruction donnée en langue naturelle (avec son lot d'ambiguïté).
- **intégration** de LLM dans des process ou pipelines qui impliquent des interactions en chaînes: 

    - Systèmes agentiques "_agentic AI_"
    - RAG

## Exemple de système d'IA complexe: les agents

Un agent est une série d'appels à un LLM : l'agent est ce qui permet d'enchaîner _input_ et _output_ jusqu'à complétion d'une tâche. Le résultat de ces interactions peut ne pas être une réponse en langue naturelle ex: activation d'une fonction. 

Autrement dit, **un agent est une "IA" qui se répond à elle-même.** 

On parlera de système agentique quand plusieurs agents interagissent.

Démonstration d'un agent : assistant à l'exploration et la création de note sur un tableau interactif de @arawjoIanarawjoSplat2026

<!-- idée: - performativité du langage : la réponse du modèle devient action (tool call) -->


## Définition hypée des IA agentiques

![Description des IA agentiques par Docker [@irwinGenAIVsAgentic2025]](img/genai_v_agenticai.png)

## Description pas hypée de l'agent conversationnel de la démo

![](img/AgentIA.png)

## Applications de chat actuelles


Depuis GPT-3.5 et sa sortie publique en décembre 2022, l'application ChatGPT ne se contente pas d'envoyer seul le prompt de l'utilisateur pour interroger le LLM: dans le prompt global, on trouve un ensemble d'instructions préliminaires (le _system prompt_) et d'informations complémentaires comme l'historique des échanges (_chat history_). 

Depuis décembre 2024, le Model Context Protocol (MCP) permet l'intégration modulaire de l'interface de chat à d'autres fonctionalités. 

![Le MCP[^mcp]](img/mcp.png)

Exemple : la fonction _search_ => **RAG**

[^mcp]: source: https://modelcontextprotocol.io/docs/getting-started/intro


# Recherche d'information et synthèse des sources

## Retrieval Augmented Generation

Limites du LLM: 

- représentation figée sur les données d'entraînement (= mémoire implicite ne peut pas être mise à jour)
- fenêtre contextuelle limitée (ajd jusque 120 000 tokens, en réalité déclin après ~30 000 tokens) 

-> perte de fiabilité

Le RAG : architecture de système d'IA qui repose sur une base de connaissance externe dans le but d'améliorer les réponses d'une IA générative sans demander d'entrainement supplémentaire (_fine tuning_).[@lewisRetrievalAugmentedGenerationKnowledgeIntensive2021] (Facebook, University College London, New York University)

---

![Superbe diagramme d'un RAG](img/rag.png)

## RAG en bref

Requête d'une base de données[^note] avec des méthodes de Recherche d'Information (TF-iDF ou similarité cosinus) + intégration des morceaux extraits au prompt. Le LLM effectue une synthèse. Ex: NotebookLM

[^note]: ou d'un moteur de recherche

## Points d'attention sur le RAG

- Jeux de données externes peut aussi être biaisé,
- Ajout de couches d'interprétation,
- Dissémination de l'information quand l'information se trouve dans plusieurs chunks,
- Angles morts quand l'information importante est dans un chunk non extrait.

# RAG des applications de chat généralistes


## Exemple: ChatGPT

> We collaborated extensively with the news industry and carefully listened to feedback from our global publisher partners, including Associated Press, Axel Springer, Condé Nast, Dotdash Meredith, Financial Times, GEDI, Hearst, Le Monde, News Corp, Prisa (El País), Reuters, The Atlantic, Time, and Vox Media. Any website or publisher can choose to appear⁠(opens in a new window) in ChatGPT search. If you’d like to share feedback, please email us at publishers-feedback@openai.com⁠.
> --- @openaiIntroducingChatGPTSearch2024

1. Reformulation de l'entrée utilisateur en une ou plusieurs requêtes
2. Requêtes envoyées à Bing et Shopify[^source] et sur leur base de données interne (médias partenaires). 
3. Re-ranking ? 
4. Réponse généré depuis le prompt contenant les informations extraites (+ system prompt, chat history etc.) 

[^source]: https://help.openai.com/en/articles/9237897-chatgpt-search#h_e40ba06c5b


-> Atlas, un navigateur avec chatGPT comme "moteur de recherche" par défaut.  @dashChatGPTsAtlasBrowser2025 parle d'un navigateur 'anti-web':

- ne retourne pas de réponse sur le web. 
- basé sur une interprétation de l'intention utilisateur vs. GUI
- autorise OpenAI à lire toutes les données lues et entrées dans le navigateur : "The idea is that ChatGPT will be your agent, but in reality you are ChatGPT's agent"

>By keeping the ChatGPT sidebar open while you browse, and giving it permission to look over your shoulder, OpenAI can suddenly access all kinds of things on the internet that they could never get to on their own.

## Exemple: Le Chat de Mistral

Partenariat avec l'AFP depuis janvier 2025 [@afpAFPMistralAI2025]. Opacité quant à la méthode de recherche d'information sur internet[^mistral]. 

[^mistral]: https://docs.mistral.ai/agents/tools/built-in/websearch


# Assistants de recherche AI 

## Qui ? quoi ?

- Google Scholar 
- SemanticScholar 
- JSTOR 
- Primo Research Assistant (spécialisé bibliothèque)
- Web of Science Research Assistant
- Scopus AI 
- Asta
- scite.ai
- undermind.ai
<!-- - reLIS de l'Udem : @bigendakoModelingToolConducting2026 -->

Qu'est-ce qu'on entend par IA dans ce cas ? 

5 à 6 niveaux d'intervention possible !

## Création de métadonnées

Désambiguisation, keywords, classification de topics, abstract. 
(OpenAlex, Isidore? -> ML pour attribution de sujets reliés). 

## Expansion de requête

1. Méthodes sans IA : thésaurus, ontologies.

2. _Query expansion_ avec un LLM: "Écrit 10 variants de la requête suivantes"

## Méthodes de Recherche d'information 

1. Méthodes classiques (non IA ?): 
    - recherche exacte[^regex] avec opérateurs booléens: 
    ex: '**citation**' retourne 'The decrease in uncited articles and its effect on the concentration of **citation**s'
    - recherche lexicale statistique: TF-iDF (_term frequency inverse document frequency_) et BM25 -> ranking de la recherche terme par rapport à sa présence dans le corpus. 
    - ex: SemanticScholar, Isidore

2. Recherche sémantique (_semantic search_/_dense retrieval_) utilisation des plongements lexicaux de modèles types encodeur (BERT) ou décodeur (e.g. GPT) lors de la recherche: représentation vectorielle de la requête et de l'entièreté de la base de données -> mesure de similarité cosinus.
    - ex: fonction "Semantic Results" de JSTOR 

3. Recherche hybride (_hybrid search_): mélange de 1. et 2. (pas forcément 50/50). 

-> Impact sur la manière de requêter: 1. par mot-clé, 2. 'en langue naturelle'. 

[^regex]: ou regex!

## Reranking

Classement des articles présentés selon un critère de pertinence par rapport à la requête. 

1. ML classique (entraînement d'un modèle au classement)

2. Comparaison de vecteurs (requête/titre de l'article): score = proximité. ex: Primo search assistant[^primo]

3. Évaluation par un LLM type 'gen AI' : prompt de classement ou catégorisation de pertinence. Fournissent les explications: Ex: Asta

---

![Asta présente la justification de la catégorie de pertinence](img/asta.png)

## Reranking (suite)

4. Ajout de critères externes Ex: semantic Scholar, "highly-cited papers"

[^primo]: Source: https://knowledge.exlibrisgroup.com/Primo/Product_Documentation/020Primo_VE/Primo_VE_(English)/015_Getting_Started_with_Primo_Research_Assistant

## Enrichissement de la liste de résultats

![Google Scholar Labs donne une explication de la présence de l'article dans la liste de résultat](img/googlescholarlabs.png)

## Synthèse des articles ou assistant de revue de littérature

Synthèse des articles extraits pour répondre à une question en langue naturelle => RAG. 

1. RAG simple: Elicit,  SciSpace (source: Semantic Scolar, Open Alex), fonction TLDR de Semantic Scholar. 

2. _Deep research_ : Agentic AI, spécialisation de plusieurs agents, retourne un rapport complet en quelques minutes. Fonctionalités spécialisés Ex: Consensus fonctionalité "Study Snapchot".  

--- 

![Undermind.ai](img/undermindai.png)

[source](https://app.undermind.ai/report/96d1ce264f5b976eac434514d16e2529a99968d6928b225d57859617b14beca1)

## Limites des outils de synthèse

- Quelles bases de données ?
- Basé sur métadonnées seulement (abstract)
- Peut inventer des sources pour répondre à une question (-> _citogenesis_ phénomène qui précède les LLM et les _lit review assistants_.)

> The AI-generated things get propagated into other real things, so students see them cited in real things and assume they’re real, and get confused as to why they lose points for using fake sources when other real sources use them [@kleeAIInventingAcademic2025]


## Overview par Aaron Tay

![Synthèse des outils d'IA [@tayWhatWeActually2025]](img/Tay_synthese_researchAssistant.png)

Pour suivre ces questions, suivre Aaron Tay : [https://aarontay.substack.com/](https://aarontay.substack.com/)


# Échanges et questions

## Prochains ateliers débogue

**Le matériel informatique : trésor ou ordure ?**
 **29 janvier, même heure même lieu**

> Rester à la fine pointe de la technologie, ça coûte cher. Mais est-ce même utile ? Est-ce que ça se fait de seulement remplacer la batterie de son ordinateur, ou un disque pour rendre sa machine plus rapide ? C’est souvent plus facile qu’on le pense ! Avec cette démo, on vous aide à garder votre machine plus longtemps, et votre argent dans vos poches ! 

**Documentation des nouvelles pratiques liées à l’utilisation de l’IA : préconisations pour les SHS** **12 mars, même heure même lieu**



## Références





















