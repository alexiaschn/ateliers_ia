import streamlit as st
import spacy
import numpy as np
from sklearn.decomposition import PCA
import plotly.express as px
import re
import pandas as pd

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

tab1, tab2 = st.tabs(['Modélisation experte', 'Vectorisation'])

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


# Premier type de modélisation
with tab1:
    st.markdown('### Modélisation experte')
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
        
    with col2: 
        if vecteurs:
            data = pd.DataFrame({
                'token' : pd.Series([token for token in doc]),
                'vecteur': pd.Series([token.vector for token in doc])
            })
            st.table(data)

        if visualisation:
            # Récupérer les vecteurs des tokens (seulement ceux qui ont un vecteur non nul)
            tokens = [token.text for token in doc if token.has_vector]
            vectors = np.array([token.vector for token in doc if token.has_vector])

            if len(tokens) < 2:
                st.warning("Pas assez de tokens avec vecteurs pour faire une projection.")
            else:
                # Réduction en 2D avec PCA
                pca = PCA(n_components=2)
                reduced = pca.fit_transform(vectors)

                # Création du DataFrame pour visualisation
                import pandas as pd
                df = pd.DataFrame({
                    "token": tokens,
                    "x": reduced[:, 0],
                    "y": reduced[:, 1]
                })

                # Visualisation interactive
                fig = px.scatter(
                    df, x="x", y="y", text="token",
                    title="Projection PCA des vecteurs de tokens",
                    width=700, height=500
                )
                fig.update_traces(textposition='top center')
                st.plotly_chart(fig)
