import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

appl = yf.Ticker("AAPL")
days = 5
input_date = str(days) + "d"
# print(appl.history(period=f'{days}d'))
hist = appl.history(period=input_date)
print(hist)