import datetime
from datetime import timedelta

import requests

from ativo.models import Ativo
from constantes import api_binance, estatistica
from historico.models import Historico, solicitar_estatistica_atual, buscar_pelo_historico
from novo import naive_bailes
from ordem.models import Ordem, buscar_pela_ordem, iniciar_ordem_compra, iniciar_ordem_venda


def check_status():
    # recuperando o objeto historic a partir da estatistica
    historico = solicitar_estatistica_atual()

    # verificar acerto de algoritmo
    historico.definindo_acerto_de_previsao()

    historico_busca = buscar_pelo_historico(historico.date)

    if historico_busca is None:
        # na primeira vez que o historico é criado, iniciamos uma compra
        historico.save()
        iniciar_ordem_compra(historico)

    else:
        # quando o historico existe atualizamos o preço do valor mais alto
        historico_busca.high = historico.high

        historico_busca.variacao = ((float(historico_busca.high) / float(historico_busca.open)) * 100) - 100

        historico_busca.save()

        iniciar_ordem_venda(historico)

        print("historico atualizado:" + str(historico.date) + str(
            datetime.datetime.fromtimestamp(float(historico.date) / 1000.0)))

    return historico
