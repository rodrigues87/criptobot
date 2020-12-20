import pandas as pd

base = pd.read_csv('btc_1h.csv')
previsores = base.iloc[:,0:2].values
classe = base.iloc[:,2].values


from sklearn.naive_bayes import GaussianNB
classificador = GaussianNB()
classificador.fit(previsores, classe)
"""
resultado = classificador.predict([23437.96])
print(classificador.classes_)
print(classificador.class_count_)
print(classificador.class_prior_)
"""