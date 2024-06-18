import pandas as pd
import altair as alt
import streamlit as st
import yfinance as yf

st.title("US Stock Price Display Application")
st.sidebar.write("""
                 ## GAFA Stock price
                 ## Visualize tool
                 """)
st.sidebar.write("Select Display days")
days = st.sidebar.slider("Days", 1, 50, 20)

st.write(f"""
         ### GAFA Stock Price past **{days} days**
         """)

@st.cache_data
def get_data(dats, tickers):
  df = pd.DataFrame()
  for company in tickers.keys():
    tkr = yf.Ticker(tickers[company])
    hist = tkr.history(period=f"{days}d")
    hist.index = hist.index.strftime("%d %B %Y")
    hist = hist[["Close"]]
    hist.columns = [company]
    hist = hist.T
    hist.index.name = "Name"
    df = pd.concat([df, hist])
  return df

try:
    st.sidebar.write("""
                    ## Stock Price Range
                    """)

    ymin, ymax = st.sidebar.slider("Input Price Range", 0.0, 3500.0, (0.0, 3500.0))

    tickers = {
        "Apple": "AAPL",
        "Facebook": "META",
        "Google": "GOOGL",
        "Microsoft": "MSFT",
        "Netflix": "NFLX",
        "Amazon": "AMZN"
    }

    df = get_data(days, tickers)
    companies = st.multiselect("Select company", list(df.index),
                            ["Google", "Facebook", "Apple", "Amazon"])

    if not companies:
        st.error("Select at least one company")
    else:
        data = df.loc[companies]
        st.write("### Stock Price US", data.sort_index())
        data = data.T.reset_index()
        data = pd.melt(data, id_vars=["Date"]).rename(
        columns={"value": "Stock Price(USD)"})

        chart = (
            alt.Chart(data)
            .mark_line(opacity=0.8, clip=True)
            .encode(
                x="Date:T",
                y=alt.Y("Stock Price(USD):Q", stack=None,
                        scale=alt.Scale(domain=[ymin, ymax])),
                color="Name:N"
        )
    )
        st.altair_chart(chart, use_container_width=True)
    
except:
    st.error("""
             Oops! Something went wrong
             """)