# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 10:24:53 2021

@author: clu1
"""

# Use streamlit to create a simple app that plots a stocks closing price
# Use the the Yahoo Finance API to collect data (or API of your choice)
# The app should have a textbox to enter stock symbol (perhaps the sidebar may work well for this)
# Also include textboxes for a start date and end date
# Display a button that when clicked graphs the chosen stock closing prices for the specified date range 
# Display a title with the company name above the chart

import streamlit as st

import datetime as dt
import pandas_datareader as pdr

today = dt.date.today()
start_date = today - dt.timedelta(days=365)
st.sidebar.header("User Inputs")


def user_inputs():
    ticker = st.sidebar.text_input('Ticker')
    start = st.sidebar.text_input('Start Date')
    end = st.sidebar.text_input('End Date')
    button = st.sidebar.button('Get Chart')
    return ticker, start, end, button


ticker, start, end, button = user_inputs()

st.write('#', ticker)

def get_symbol(ticker, start=start, end=end):
    symbol = ticker.upper()
    data = pdr.get_data_yahoo(ticker, start, end)
    return data

if button:
    data = get_symbol(ticker)
    st.line_chart(data.Close)