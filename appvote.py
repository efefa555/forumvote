import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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
fig_profil, ax_profil = plt.subplots()
sns.countplot(data=df, x='Profil', ax=ax_profil)
st.pyplot(fig_profil)

st.subheader("Évaluation de la réputation de l’EHTP")
fig_reputation, ax_reputation = plt.subplots()
sns.histplot(data=df, x='Reputation', hue='Profil', multiple='stack', ax=ax_reputation)
st.pyplot(fig_reputation)

st.subheader("Évaluation de la qualité académique")
fig_qualite, ax_qualite = plt.subplots()
sns.histplot(data=df, x='Qualite', hue='Profil', multiple='stack', ax=ax_qualite)
st.pyplot(fig_qualite)

st.subheader("Évaluation de l’innovation")
fig_innovation, ax_innovation = plt.subplots()
sns.histplot(data=df, x='Innovation', hue='Profil', multiple='stack', ax=ax_innovation)
st.pyplot(fig_innovation)

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