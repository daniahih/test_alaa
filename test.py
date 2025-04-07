import streamlit as st
import pandas as pd
import numpy as np  

st.title('Streamlit Example')
st.subheader('This is a subheader') 

st.markdown("[link to my portfolio ](https://github.com/daniahih/stream_lit-)")
st.subheader('Line Chart')
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
st.line_chart(chart_data)
st.subheader('Area Chart')