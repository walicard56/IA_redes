# Coleta de comentários do YouTube com youtube-comment-downloader
# Instale com: pip install youtube-comment-downloader

from youtube_comment_downloader import YoutubeCommentDownloader
import pandas as pd

def coletar_comentarios_youtube(video_url, max_comentarios=100):
    downloader = YoutubeCommentDownloader()
    comments = downloader.get_comments_from_url(video_url, sort_by="top")
    resultados = []
    for i, comment in enumerate(comments):
        if i >= max_comentarios:
            break
        resultados.append([comment['text'], comment['author'], comment['time']])
    df = pd.DataFrame(resultados, columns=["Texto", "Autor", "Data"])
    df.to_csv("comentarios_youtube.csv", index=False)
    print("Comentários salvos em comentarios_youtube.csv")

# Exemplo de uso:
# coletar_comentarios_youtube("https://www.youtube.com/watch?v=ID_DO_VIDEO", 50)