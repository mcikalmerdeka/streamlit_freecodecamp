import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of Google!
""")

# define the ticker symbol
tickerSymbol = 'GOOGL'

try:
    # get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)
    # get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
    
    if not tickerDf.empty:
        st.line_chart(tickerDf.Close)
        st.line_chart(tickerDf.Volume)
    else:
        st.error("No data received from yfinance")
        
except Exception as e:
    st.error(f"An error occurred: {str(e)}")
