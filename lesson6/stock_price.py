import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

appl = yf.Ticker("AAPL")
days = 1
input_date = str(days) + "mo"
tickers = {
    "apple": "AAPL",
    "facebook": "Meta"
}
# print(appl.history(period=f'{days}d'))
for company in tickers.keys():
    stock_hist = yf.Ticker(tickers[company])
    hist = stock_hist.history(period=input_date)

    hist.index = hist.index.strftime("%d %B %Y")
    hist = hist[['Close']]
    hist.columns = [company]
    hist = hist.T
    hist.index.name = "Name"


