import ccxt

from pprint import pprint

exchange = ccxt.kucoin()
ticker = exchange.fetch_ticker('XRP/USDT')
pprint(exchange.last_http_response)
pprint(exchange.last_json_response)
