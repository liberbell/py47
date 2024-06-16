import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

appl = yf.Ticker("AAPL")
days = 1
input_date = str(days) + "mo"
# print(appl.history(period=f'{days}d'))
hist = appl.history(period=input_date)

hist.index = hist.index.strftime("%d %B %Y")
hist = hist[['Close']]
hist.columns = ['Apple']
print(hist)