# Classificador de sentimento simples com TF-IDF + LogisticRegression
# Instale com: pip install scikit-learn pandas

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib

def treinar_modelo(csv_path):
    df = pd.read_csv(csv_path)
    X = df['texto']
    y = df['sentimento']

    vectorizer = TfidfVectorizer()
    X_vect = vectorizer.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_vect, y, test_size=0.2, random_state=42)
    modelo = LogisticRegression()
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)
    print(classification_report(y_test, y_pred))

    joblib.dump(modelo, 'modelo_sentimento.pkl')
    joblib.dump(vectorizer, 'vetorizador_tfidf.pkl')
    print("Modelo e vetorizador salvos!")

def prever_sentimento(textos):
    modelo = joblib.load('modelo_sentimento.pkl')
    vectorizer = joblib.load('vetorizador_tfidf.pkl')
    textos_vect = vectorizer.transform(textos)
    return modelo.predict(textos_vect)

# Exemplo:
# treinar_modelo("dataset_sentimentos.csv")
# print(prever_sentimento(["achei o filme maravilhoso", "essa música é horrível"]))