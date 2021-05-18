import ccxt
from ccxt.base.exchange import Exchange

binance_exchange = ccxt.binance({
    'timeout':15000,
    'enableRateLimit':True
})

print('交易所id：', binance_exchange.id)
print('交易所名称：', binance_exchange.name)

binance_exchange.load_markets()
symbol = 'BTC/USDT'
binance_tickers = binance_exchange.fetch_tickers(symbol)
print(binance_tickers)



ftx_exchange = ccxt.ftx({
    'timeout':15000,
    'enableRateLimit':True
})

print('交易所id：', ftx_exchange.id)
print('交易所名称：', ftx_exchange.name)

ftx_exchange.load_markets()
symbol = 'BTC/USDT'
ftx_tickers = ftx_exchange.fetch_tickers(symbol)
print(ftx_tickers)



 
