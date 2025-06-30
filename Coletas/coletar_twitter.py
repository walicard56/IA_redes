# Coleta de tweets usando snscrape (não precisa API)
# Instale com: pip install snscrape

import snscrape.modules.twitter as sntwitter
import pandas as pd

def coletar_tweets(palavra_chave, max_tweets=100):
    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(palavra_chave).get_items()):
        if i >= max_tweetss:
            break
        tweets.append([tweet.date, tweet.content, tweet.user.username])
    df = pd.DataFrame(tweets, columns=['Data', 'Texto', 'Usuário'])
    df.to_csv('tweets_coletados.csv', index=False)
    print("Tweets salvos em tweets_coletados.csv")

# Exemplo de uso:
# coletar_tweets("inteligência artificial", 50)