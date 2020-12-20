import requests
from django.shortcuts import render

from constantes import api_binance, estatistica

from novo import naive_bailes


def atualizar_ativo():
    response = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=BTCUSDT')
    ativo = response.json()


def home(request):
    global compra, precisao
    atualizar_ativo()
    response = requests.get('https://api1.binance.com/api/v3/ticker/price?symbol=BTCUSDT')
    url = api_binance + estatistica("BTCUSDT")
    response2 = requests.get(api_binance + estatistica("BTCUSDT"))
    array = response2.json()
    for item in array:
        data = item[0]
        open = item[1]

        retorno = naive_bailes(data, open)
        precisao = retorno[0]

        value = retorno[1]

        if retorno[1][0] == 0:
            compra = "Não"
        else:
            compra = "Sim"

    ativo = response.json()

    return render(request, "main/home.html", {"ativo": ativo, "compra": compra, "precisao":precisao})
