# Exemplo simples de scraping de blogs usando requests + BeautifulSoup
# Instale com: pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup
import pandas as pd

def coletar_posts_blog(url, max_posts=5):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    posts = soup.find_all('article')[:max_posts]
    resultados = []
    for post in posts:
        titulo = post.find('h2') or post.find('h3')
        if titulo:
            resultados.append([titulo.text.strip(), url])
    df = pd.DataFrame(resultados, columns=["Título", "Fonte"])
    df.to_csv("posts_blog.csv", index=False)
    print("Posts de blog salvos em posts_blog.csv")

# Exemplo de uso:
# coletar_posts_blog("https://blog.google/", 5)