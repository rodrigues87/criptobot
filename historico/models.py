from django.db import models
import datetime

# Create your models here.
from constantes import api_binance, estatistica
import requests

from novo import naive_bailes


def criar_historico(hitorico):
    historico = Historico.objects.create(date=hitorico.data, open=hitorico.open, high=hitorico.high,
                                         previsao=hitorico.previsao)
    print("novo historico salvo:" + str(historico.date) + str(
        datetime.datetime.fromtimestamp(float(historico.date) / 1000.0)))
    return historico


def buscar_pelo_historico(data):
    try:
        historico = Historico.objects.get(date=data)
        #print("O histórico  existe")

        return historico
    except Historico.DoesNotExist:
        print("O histórico não existe")
        return None


def solicitar_estatistica_atual():
    historico = Historico()

    url = api_binance + estatistica("BTCUSDT")
    response = requests.get(url)
    array = response.json()
    for item in array:
        historico.date = item[0]
        historico.open = float(item[1])
        historico.high = float(item[2])
        historico.low = float(item[3])
        historico.close = item[4]

    historico.previsao = montar_previsao_de_historico(historico)

    return historico


def montar_previsao_de_historico(historico):
    retorno = naive_bailes(historico.date, historico.open)
    previsao = retorno[1][0]
    return previsao


class Historico(models.Model):
    date = models.CharField(max_length=40)
    open = models.DecimalField(max_digits=20, decimal_places=2)
    high = models.DecimalField(max_digits=20, decimal_places=2)
    previsao = models.BooleanField()
    acertou = models.BooleanField(null=True, blank=True)
    variacao = models.DecimalField(max_digits=3, decimal_places=1,null=True, blank=True)

    def definindo_acerto_de_previsao(self):

        self.variacao = ((self.high / self.open) * 100) - 100

        if self.variacao >= 1.5 and self.previsao == 1:
            self.acertou = 1
        if self.variacao < 1.5 and self.previsao == 1:
            self.acertou = 0
        if self.variacao < 1.5 and self.previsao == 0:
            self.acertou = 1
        if self.variacao > 1.5 and self.previsao == 0:
            self.acertou = 0

    def __str__(self):
        return self.date
