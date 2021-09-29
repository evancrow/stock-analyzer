import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials

spy = yf.download("spy")
print(spy)