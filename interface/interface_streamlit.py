# Interface Streamlit para análise de sentimento
# Instale: pip install streamlit joblib

import streamlit as st
import joblib

st.set_page_config(page_title="Análise de Sentimento IA", layout="centered")

st.title("🔍 Análise de Sentimento com IA")
st.write("Digite um texto e veja se a IA acha que é positivo, negativo ou neutro.")

modelo = joblib.load("modelo_sentimento.pkl")
vectorizer = joblib.load("vetorizador_tfidf.pkl")

texto_input = st.text_area("Digite seu texto aqui", height=150)

if st.button("Analisar Sentimento"):
    if texto_input.strip() == "":
        st.warning("Por favor, digite algum texto.")
    else:
        texto_vect = vectorizer.transform([texto_input])
        pred = modelo.predict(texto_vect)[0]
        st.success(f"🎯 Sentimento detectado: **{pred.upper()}**")