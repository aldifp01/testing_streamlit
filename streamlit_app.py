import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title('Hasil Balapan Orang Paling Rasis di F1')
racist=pd.read_csv("racistTr.csv",sep=",")
alt.Chart(racist).transform_fold(
    ['Charles Leclerc', 'Max Verstappen', 'Lewis Hamilton']
).mark_bar().encode(
    x='Laps',
    y='Racist',
    color='key:N'
)

st.markdown("""Charles Leclerc adalah yang paling rasis di Bahrain 2022.""")
