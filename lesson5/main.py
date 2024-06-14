import streamlit as st
import numpy as np
import pandas as pd

st.title("Streamlit introduction")
st.write("DataFrame")

df = pd.DataFrame({
    "1stline": [1, 2, 3, 4, 5],
    "2ndline": [10, 20, 30, 40, 50],
})

st.dataframe(df)