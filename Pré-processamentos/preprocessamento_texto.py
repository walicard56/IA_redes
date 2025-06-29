# Pré-processamento de texto com NLTK
# Instale com: pip install nltk unidecode

import re
import nltk
import unidecode

nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stopwords_pt = set(stopwords.words('portuguese'))

def limpar_texto(texto):
    texto = texto.lower()
    texto = unidecode.unidecode(texto)  # remover acentos
    texto = re.sub(r"http\S+|www\S+|[^a-zA-Z\s]", "", texto)  # remover URLs e pontuações
    tokens = word_tokenize(texto)
    tokens_filtrados = [t for t in tokens if t not in stopwords_pt and len(t) > 2]
    return " ".join(tokens_filtrados)

# Exemplo:
# print(limpar_texto("O governo está ótimo! Visite http://site.com"))