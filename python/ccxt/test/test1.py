import ccxt
from ccxt.base.exchange import Exchange
from tkinter import *

symbol = 'ETH/USDT'

# FTX -----------------------------------------------
ftx_exchange = ccxt.ftx({
    'timeout':15000,
    'enableRateLimit':True
})

print('交易所id：', ftx_exchange.id)
print('交易所名称：', ftx_exchange.name)

ftx_exchange.load_markets()
#symbol = 'BTC/USDT'
ftx_tickers = ftx_exchange.fetch_tickers(symbol)
#print(ftx_tickers)
#print(type(ftx_tickers))

ftx_close_price =  ftx_tickers[symbol]['close']

print("bid: " , ftx_tickers[symbol]['bid'])
print("close: " , ftx_close_price)
print("ask: " , ftx_tickers[symbol]['ask'])


# Binance -----------------------------------------------
binance_exchange = ccxt.binance({
    'timeout':15000,
    'enableRateLimit':True
})

print('交易所id：', binance_exchange.id)
print('交易所名称：', binance_exchange.name)

binance_exchange.load_markets()

binance_tickers = binance_exchange.fetch_tickers(symbol)
#print(binance_tickers)
binance_close_price =  binance_tickers[symbol]['close']
print("bid: " ,binance_tickers[symbol]['bid'])
print("close: " ,binance_close_price)
print("ask: " ,binance_tickers[symbol]['ask'])

if ( ftx_close_price >= binance_close_price ):
    percentage = ((ftx_close_price - binance_close_price) / binance_close_price )
else:
    percentage = (( binance_close_price - ftx_close_price) / binance_close_price )

print("percentage = " ,percentage)

tk =Tk()
tk.geometry("300x160")
canvas = Canvas(tk, width=640, height= 480)
canvas.pack()
canvas.create_line(100,100,320,640)

tk.mainloop()