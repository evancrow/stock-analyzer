import yfinance as yf
from yahoofinancials import YahooFinancials
from pricePoint import PricePoint

# MOCK DATA
def getFormattedDataFor(ticker, start=None, end=None):
    return formatDataAsPricePoint(downloadDataFor(ticker, start, end))


def downloadDataFor(ticker, start = None, end = None):
    if start is None or end is None:
        return yf.download(ticker)
    else:
        return yf.download(ticker, start=start, end=end)

# Returns data from yFinance as an array of PricePoint objects
def formatDataAsPricePoint(data):
    formattedData = []
    data.reset_index(inplace = True)

    for index, close in enumerate(data['Close']):
        date = (data['Date'][index]).strftime("%x")
        formattedData.append(PricePoint(close, date))

    return formattedData

# COMMODITY AND CURRENCY
def getFormattedDataForCommodity(currency, start=None, end=None):
    return formatDataAsPricePointForCommodity(currency, downloadDataForCommodity(currency, start, end))

def downloadDataForCommodity(currency, start = None, end = None):
    currencies = YahooFinancials([currency])

    if start is None or end is None:
        return currencies.get_historical_price_data()
    else:
        return currencies.get_historical_price_data(start, end, "daily")

def formatDataAsPricePointForCommodity(currency, data):
    formattedData = []
    prices = data[currency]['prices']

    for price in prices:
        formattedData.append(PricePoint(price['close'], price['formatted_date']))

    return formattedData

# TESTING
spy = getFormattedDataForCommodity("EUR", start="2019-01-01", end="2020-01-01")
print(spy)
