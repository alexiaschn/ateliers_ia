import streamlit as st
import spacy
import numpy as np
from sklearn.decomposition import PCA
import plotly.express as px
import re
import pandas as pd
from ollama import chat, ChatResponse, create

# Configuration
nlp = spacy.load("fr_core_news_md")

st.set_page_config(layout='wide',
    initial_sidebar_state="expanded",
    page_title="Démo ateliers",
)

def get_demo_type():
    if 'demo_type' not in st.session_state:
        st.session_state.demo_type = 'expert'
    return st.session_state['demo_type']

# Structure de la page
st.title("Démonstration pour les ateliers IA pour SHS")
# Entrée utilisateur
phrase = st.text_input("Entrez une phrase")
doc = nlp(phrase)

tab1, tab2, tab3 = st.tabs(['Approche symbolique', 'Vectorisation', 'Ollama'])

# Fonctions de modélisation

def expert_class(doc): 
    # motif qui ignore la casse et inclus le pluriel
    fruit_pattern = re.compile('(pomme|poire|banane|orange|clémentine|raisin|bleuet)s?', flags=re.IGNORECASE)
    # on regarde chaque token dans la phrase
    for token in doc: 
        # est-ce que l'un des tokens est dans la liste de fruit
        if fruit_pattern.match(token.text.lower()): 
            # si le fruit est un adjectif alors c'est la couleur orange.
            if token.pos_ == 'ADJ': 
                return False
            else:
                return True
    return False

def visualisation_2d(doc, doc2=None):
    tokens, vectors, sources = [], [], []

    # First doc
    for token in doc:
        if token.has_vector:
            tokens.append(token.text)
            vectors.append(token.vector)
            sources.append("Doc1")

    # Second doc (optional)
    if doc2 is not None:
        for token in doc2:
            if token.has_vector:
                tokens.append(token.text)
                vectors.append(token.vector)
                sources.append("Doc2")

    # Not enough tokens?
    if len(vectors) < 2:
        st.warning("Pas assez de tokens avec vecteurs pour faire une projection.")
        return

    # PCA to 2D
    vectors = np.array(vectors)
    pca = PCA(n_components=2)
    reduced = pca.fit_transform(vectors)

    # DataFrame for visualization
    df = pd.DataFrame({
        "token": tokens,
        "x": reduced[:, 0],
        "y": reduced[:, 1],
        "source": sources
    })

    # Interactive scatter plot
    fig = px.scatter(
        df, x="x", y="y", text="token", color="source",
        title="Projection PCA des vecteurs de tokens",
        width=700, height=500
    )
    fig.update_traces(textposition="top center")

    st.plotly_chart(fig)

# Premier type de modélisation
with tab1:
    col1, col2 = st.columns(2)
    with col1:
        classification_fruit = st.button('Classification fruit')
        tokenisation = st.button('Tokenisation')
        ner = st.button('Entités Nommées')
        pos = st.button('POS-tagging')
    with col2:
        if classification_fruit:
            st.write(f'La phrase "{phrase}" parle de fruit : **{expert_class(doc)}**')
            with st.expander('Ouvrir pour voir le code'):
                st.markdown(f"""```
        def expert_class(doc): 
        # motif qui ignore la casse et inclus le pluriel
        fruit_pattern = re.compile('(pomme|poire|banane|orange|clémentine|raisin|bleuet)s?', flags=re.IGNORECASE)
        # on regarde chaque token dans la phrase
        for token in doc: 
            # est-ce que l'un des tokens est dans la liste de fruit
            if fruit_pattern.match(token.text.lower()): 
                # si le fruit est un adjectif alors c'est la couleur orange.
                if token.pos_ == 'ADJ': 
                    return False
                else:
                    return True
        return False```""")
        if tokenisation:
            data = pd.DataFrame({'basic tokenisation': pd.Series(phrase.split()), 
                'spaCy tokenisation': pd.Series([token.text for token in doc])
                
                }).fillna('')
            st.table(data)
        if ner: 
            data = pd.DataFrame({
            'Entités Nommées': pd.Series([ent.text for ent in doc.ents]),
            'Type': pd.Series([ent.label_ for ent in doc.ents])})
            st.table(data)
            
        if pos: 

            data = pd.DataFrame({
            'Token': pd.Series([tok for tok in doc]),
            'Part of Speech Tag': pd.Series([tok.pos_ for tok in doc])})
            st.table(data)


with tab2:
    col1, col2 = st.columns(2)
    with col1:
        vecteurs = st.button('Vecteurs')
        visualisation = st.button("Visualiser l'espace vectoriel") 
        with st.form("compare_form"):
            phrase2 = st.text_input("Deuxième phrase à comparer")
            submitted = st.form_submit_button("Comparer")
        
    with col2: 
        if vecteurs:
            data = pd.DataFrame({
                'token' : pd.Series([token for token in doc]),
                'vecteur': pd.Series([token.vector for token in doc])
            })
            st.table(data)

        if visualisation:
            visualisation_2d(doc)
        if submitted and phrase2.strip():
            st.write(f"""Comparaison des vecteurs des phrases : "{phrase}" et "{phrase2}" """)
            doc2 = nlp(phrase2)
            visualisation_2d(doc, doc2)
with tab3:
    # --- initialize the list of models once ---
    if "models" not in st.session_state:
        st.session_state.models = ["llama3.2", "Steer un model"]

    # let user pick
    model = st.selectbox(
        "Quel LLM utiliser ?",
        st.session_state.models,
        index=None,
        placeholder="Choisir un modèle"
    )

    # if user wants to steer/create a new model
    if model == "Steer un model":
        with st.form("system_instruction_form"):
            instruction = st.text_input("Entrez l'instruction système")
            new_model = st.text_input("Donner un nom au nouveau modèle")
            instruction_submitted = st.form_submit_button("Créer nouveau modèle")

            if instruction_submitted and new_model:
                # create the model
                create(model=new_model, from_="llama3.2", system=instruction)
                # add it to the list if not already there
                if new_model not in st.session_state.models:
                    st.session_state.models.insert(0, new_model)  # insert at top
                st.success(f"Modèle '{new_model}' créé et ajouté à la liste.")
                st.rerun()

    # if a real model is selected (existing or new) and phrase exists
    if model and model != "Steer un model" and phrase is not None:
        stream = chat(model=model, messages=[{"role": "user", "content": phrase}], stream=True)

        placeholder = st.empty()
        full_text = ""

        for chunk in stream:
            if "message" in chunk and "content" in chunk["message"]:
                full_text += chunk["message"]["content"]
                placeholder.markdown(full_text)
