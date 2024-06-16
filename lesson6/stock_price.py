import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

appl = yf.Ticker("AAPL")
days = 20
# print(appl.history(period=f'{days}d'))
print(appl.history(period=f"{days}d"))