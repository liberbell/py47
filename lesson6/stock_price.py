import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import altair as alt

appl = yf.Ticker("AAPL")
days = 1
input_date = str(days) + "mo"
tickers = {
    "apple": "AAPL",
    "facebook": "Meta",
    "nvidia": "NVDA",
    "microsoft": "MSFT",
    "google": "GOOGL",
    "netflix": "NFLX",
}

def get_data(input_date, tickers):
    df = pd.DataFrame()

    for company in tickers.keys():
        stock_hist = yf.Ticker(tickers[company])
        hist = stock_hist.history(period=input_date)

        hist.index = hist.index.strftime("%d %B %Y")
        hist = hist[['Close']]
        hist.columns = [company]
        hist = hist.T
        hist.index.name = "Name"
        df = pd.concat([df, hist])
    
    return df

# print(get_data(input_date, tickers))
companies = ["apple", "facebook"]

df = get_data(input_date, tickers)

data = df.loc[companies]
print(data.sort_index())
print(data.T.reset_index())

data = pd.melt(data, id_vars=["Date"]).rename(
        columns={"value": "Stock Price(USD)"}
        )

# print(data2.columns)
# data3 = pd.melt(data2, id_vars=['Date']).rename(
#     columns = {"values": "Stock Price(USD)"}
# )
# print(data3)


