api_binance = "https://api1.binance.com/"
preco_atual = "api/v3/ticker/price?symbol="


def estatistica(symbol):
    return "api/v3/klines?symbol=" + symbol + "&interval=1h&limit=1"
