from django.db import models
from constantes import api_binance, preco_atual
import requests


class Ativo(models.Model):
    nome = models.CharField(max_length=40, unique=True)
    sigla = models.CharField(max_length=10, unique=True)
    valor_de_mercado = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)

    def verificar_valor_de_mercado(self):
        url = api_binance + preco_atual + "BTCUSDT"
        response = requests.get(url)

        self.valor_de_mercado = response.json()["price"]
        self.save()

    def __str__(self):
        return self.nome
