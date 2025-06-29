# Avaliação de modelo de sentimento com métricas e gráficos
# Instale: pip install scikit-learn matplotlib seaborn pandas

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix

def avaliar_modelo(y_true, y_pred, nome_modelo="Modelo"):
    print(f"\n=== Avaliação: {nome_modelo} ===")
    print(classification_report(y_true, y_pred))

    cm = confusion_matrix(y_true, y_pred, labels=list(set(y_true)))
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=list(set(y_true)), yticklabels=list(set(y_true)))
    plt.xlabel('Predito')
    plt.ylabel('Verdadeiro')
    plt.title(f'Matriz de Confusão - {nome_modelo}')
    plt.tight_layout()
    plt.savefig('matriz_confusao.png')
    plt.show()

# Exemplo:
# avaliar_modelo(y_test, y_pred)