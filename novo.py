import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score


def naive_bailes(data,open):
    base = pd.read_csv('btc_usd.csv')

    previsores = base.iloc[:, 0:2].values
    classe = base.iloc[:, 3].values

    scaler = StandardScaler()
    previsores = scaler.fit_transform(previsores)

    previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe,
                                                                                                  test_size=0.25,
                                                                                                  random_state=0)
    classificador = GaussianNB()
    classificador.fit(previsores_treinamento, classe_treinamento)

    previsoes = classificador.predict(previsores_teste)

    precisao = accuracy_score(classe_teste, previsoes)
    matriz = confusion_matrix(classe_teste, previsoes)

    atributos = [[data, open]]

    previsao_atual = classificador.predict(scaler.fit_transform(atributos))

    resposta = [precisao,previsao_atual]

    return resposta


