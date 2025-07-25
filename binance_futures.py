import ccxt
from config import BINANCE_API_KEY, BINANCE_SECRET_KEY

def place_order(symbol, side, amount):
    exchange = ccxt.binance({
        "apiKey": BINANCE_API_KEY,
        "secret": BINANCE_SECRET_KEY
    })
    exchange.create_order(symbol=symbol, type="market", side=side, amount=amount)
