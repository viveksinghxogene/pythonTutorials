import streamlit as st
import pandas as pd

st.header("Data Table Demo")

data = {"Name": ["Vivek", "Deepak"], "Score": [85, 90]}
df = pd.DataFrame(data)

st.dataframe(df)

st.header("Image Demo")

st.image("crops.jpg", caption="idk")