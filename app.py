import streamlit as st

x = st.slider("x value:", 0, 100)
y = x + 10
st.write('x + 10 = ', y)
