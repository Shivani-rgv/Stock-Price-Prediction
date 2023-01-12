import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import pandas_datareader as data
from keras.models import load_model
import streamlit as st


# start = '2010-01-01'
# end = '2019-12-31'

"""
# Stock Prediction Webapp   """ 
st.subheader('By Shivani Raghav and Prince Yadav :sunglasses')
st.write('a webapp in python made in streamlit which predict diffrent stock prices in Python using LSTM model')
# App title

st.markdown('''
- Built in `Python` using `streamlit`,`yfinance`, `keras`, `pandas` , `LSTM` and `datetime`
''')
st.write('---')
st.image("C://Users//DELL//Desktop//stock prediction//stocks.jpg", caption='Stock Prediction webapp',use_column_width=True)

# Sidebar
st.sidebar.subheader('Query parameters')
start = st.sidebar.date_input("Start date", datetime.date(2010, 1, 1))
end = st.sidebar.date_input("End date", datetime.date(2021, 1, 31))

#df = data.DataReader('AAPL','yahoo',start,end)
ticker_list = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/s-and-p-500-companies/master/data/constituents_symbols.txt')
df= data.DataReader(ticker_list,start,end)