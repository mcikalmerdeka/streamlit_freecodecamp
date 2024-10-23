import yfinance as yf
print("yfinance imported successfully")
ticker = yf.Ticker("AAPL")
print(ticker.info['regularMarketPrice'])