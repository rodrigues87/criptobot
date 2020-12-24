import datetime
from datetime import timedelta

import requests

from ativo.models import Ativo
from constantes import api_binance, estatistica
from historico.models import Historico
from novo import naive_bailes
from ordem.models import Ordem


def check_status():
    global historico
    url = api_binance + estatistica("BTCUSDT")
    response2 = requests.get(url)
    array = response2.json()
    for item in array:
        data = item[0]
        open = float(item[1])
        high = float(item[2])
        low = float(item[3])
        close = item[4]

        resultado = ((high / open) * 100) - 100
        if resultado > 1.5:
            aumentou = 1
        else:
            aumentou = 0

        try:
            historico = Historico.objects.get(date=data)
            historico.high = high
            if historico.previsao == aumentou:
                historico.acertou = 1
            else:
                historico.acertou = 0
            historico.save()
            print("historico atualizado:" + str(historico.date) + str(
                datetime.datetime.fromtimestamp(float(historico.date) / 1000.0)))

        except Historico.DoesNotExist:
            retorno = naive_bailes(data, open)
            previsao = retorno[1][0]

            historico = Historico.objects.create(date=data, open=open, high=high, previsao=previsao)
            historico.save()

            #if previsao == 1:
            #    #TODO PRECISO TRATAR CASO NÃO EXISTA
            #    ativo = Ativo.objects.get(nome="BTCUSDT")
            #    ativo.verificar_valor_de_mercado()

#                ordem = Ordem.objects.create(ativo=ativo, valor_compra=ativo.valor_de_mercado, data_compra=data)
#                ordem.abrir_ordem_compra()

            print("novo historico salvo:" + str(historico.date) + str(
                datetime.datetime.fromtimestamp(float(historico.date) / 1000.0)))

    return historico
