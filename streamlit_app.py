import streamlit as st

import pandas

df = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

df = df.set_index('Fruit')

fruits_selected = st.multiselect("Select fruit:", list(df.index), ['Avocado', 'Strawberries'])

df_to_show = df.loc[fruits_selected]

st.dataframe(df_to_show)
