import streamlit as st
import pandas as pd
import os

# Set up the initial dataframe
if os.path.exists('feedback.csv'):
    df = pd.read_csv('feedback.csv')
else:
    df = pd.DataFrame(columns=['Profil', 'Reputation', 'Qualite', 'Innovation', 'Suggestions'])

# Title of the application
st.title("Feedback Forum EHTP-Entreprises")

# Formulaire de feedback
st.header("Formulaire de feedback")
with st.form(key='feedback_form'):
    profil = st.selectbox("Quel est votre profil ?", ["Étudiant", "Recruteur", "Alumni", "Autre"])
    reputation = st.slider("Sur une échelle de 1 à 5, comment évaluez-vous la réputation de l’EHTP ?", 1, 5)
    qualite = st.slider("Sur une échelle de 1 à 5, comment évaluez-vous la qualité académique de l’EHTP ?", 1, 5)
    innovation = st.slider("Sur une échelle de 1 à 5, comment évaluez-vous l’innovation à l’EHTP ?", 1, 5)
    suggestions = st.text_area("Avez-vous des suggestions pour améliorer l’image de l’EHTP ?")
    submit_button = st.form_submit_button(label='Soumettre')

# Sauvegarde des données
if submit_button:
    new_data = {'Profil': profil, 'Reputation': reputation, 'Qualite': qualite, 'Innovation': innovation, 'Suggestions': suggestions}
    df = df.append(new_data, ignore_index=True)
    df.to_csv('feedback.csv', index=False)
    st.success("Merci pour votre feedback !")

# Affichage des résultats en temps réel
st.header("Résultats en temps réel")
st.subheader("Nombre total de votes")
st.write(len(df))

# Graphiques interactifs
st.subheader("Répartition des votes par profil")
st.bar_chart(df['Profil'].value_counts())

st.subheader("Évaluation de la réputation de l’EHTP")
st.bar_chart(df['Reputation'].value_counts().sort_index())

st.subheader("Évaluation de la qualité académique")
st.bar_chart(df['Qualite'].value_counts().sort_index())

st.subheader("Évaluation de l’innovation")
st.bar_chart(df['Innovation'].value_counts().sort_index())

# Tableau de bord interactif
st.header("Tableau de bord interactif")
st.subheader("Filtrer les résultats par type de participant")
filtre_profil = st.selectbox("Sélectionnez un profil pour filtrer", ["Tous"] + df['Profil'].unique().tolist())
if filtre_profil != "Tous":
    df_filtered = df[df['Profil'] == filtre_profil]
else:
    df_filtered = df

st.subheader("Statistiques globales")
st.write(df_filtered.describe())

st.subheader("Suggestions des participants")
st.write(df_filtered[['Profil', 'Suggestions']])