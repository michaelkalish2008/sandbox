import streamlit as st
import numpy as np
import pandas as pd

st.header('UC Berkeley, MIDS')
st.subheader('Just an app')

sb = st.sidebar.radio('Select an operation',['*','/','+','-'])

x = st.sidebar.number_input('Pick a number', 1, 10)
y = st.sidebar.number_input('Pick another number', 1, 10)
z = 0

if sb == '*':
    z = x * y
elif sb == '/':
    numerator = st.sidebar.radio('Which number should be the numerator?',[x,y])
    if numerator == x:
        z = x / y
    else:
        z = y / x
elif sb == '+':
    z = x + y
elif sb == '-':
    start_number = st.sidebar.radio('Which number should we subtract from?',[x,y])
    if start_number == x:
        z = x - y
    else:
        z = y - x

st.balloons()
st.write(f'The answer to your problem is {z}')

