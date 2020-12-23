import datetime

import requests

from constantes import api_binance, estatistica
from historico.models import Historico


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
            historico.aumentou = aumentou
            historico.save()
            print("historico atualizado:" + str(historico.date) + str(
                datetime.datetime.fromtimestamp(float(historico.date) / 1000.0)))

        except Historico.DoesNotExist:
            historico = Historico.objects.create(date=data, open=open, high=high, aumentou=aumentou)
            historico.save()
            print("novo historico salvo:" + str(historico.date) + str(
                datetime.datetime.fromtimestamp(float(historico.date) / 1000.0)))

    return historico
