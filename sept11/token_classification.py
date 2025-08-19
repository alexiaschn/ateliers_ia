import streamlit as st
import spacy
import numpy as np
from sklearn.decomposition import PCA
import plotly.express as px

# Charger le modèle français de spaCy (avec vecteurs, attention : "fr_core_news_sm" a des vecteurs très limités)
# Pour de meilleurs vecteurs, on peut utiliser "fr_core_news_md" ou "fr_core_news_lg"
nlp = spacy.load("fr_core_news_lg")

st.title("Vectorisation")
col1, col2 = st.columns([1,1], vertical_alignment='top')
with col1:
 # Saisie utilisateur
    phrase = st.text_input("Entrez une phrase")
    doc = nlp(phrase)

    if st.button('Entités Nommées'): 
        for ent in doc.ents:
            st.write((ent.text, ent.label_))
    if st.button('POS-tagging'): 
        for token in doc:
            st.write((token.text, token.pos_))
    if st.button('Vecteurs'):
        for token in doc:
            st.write(token.vector)
    if st.button("Visualiser l'espace vectoriel") and phrase.strip():
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

with col2: 
        # Saisie utilisateur
    phrase2 = st.text_input("Entrez une AUTRE phrase")
    doc2 = nlp(phrase2)

    if st.button('Entités Nommées 2'): 
        for ent in doc2.ents:
            st.write((ent.text, ent.label_))
    if st.button('POS-tagging 2'): 
        for token in doc2:
            st.write((token.text, token.pos_))

    if st.button("Visualiser l'espace vectoriel 2") and phrase.strip():
        # Récupérer les vecteurs des tokens (seulement ceux qui ont un vecteur non nul)
        tokens = [token.text for token in doc2 if token.has_vector]
        vectors = np.array([token.vector for token in doc2 if token.has_vector])

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
