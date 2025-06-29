# Coleta de manchetes via RSS feed com feedparser
# Instale com: pip install feedparser

import feedparser
import pandas as pd

def coletar_noticias(rss_url, max_noticias=50):
    feed = feedparser.parse(rss_url)
    noticias = []
    for i, entry in enumerate(feed.entries[:max_noticias]):
        noticias.append([entry.title, entry.link, entry.published])
    df = pd.DataFrame(noticias, columns=["Título", "Link", "Data"])
    df.to_csv("noticias_coletadas.csv", index=False)
    print("Notícias salvas em noticias_coletadas.csv")

# Exemplo de uso:
# coletar_noticias("https://g1.globo.com/rss/g1/", 50)