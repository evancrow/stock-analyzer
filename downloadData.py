import numpy as np
import pandas as pd
import yfinance as yf
import pickle
from IPython.display import display
from yahoofinancials import YahooFinancials

data = yf.download("AMZN AAPL GOOG", start="2017-01-01", end="2017-04-30")

# df = pd.DataFrame(data.data, columns=data.feature_names)

display(data.to_string())
stockData = open("stockData.txt", "w")


stockData.write(data.to_string())
