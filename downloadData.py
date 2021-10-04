import yfinance as yf
from pricePoint import PricePoint

# FOR MOCK DATA
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


# TESTING
spy = getFormattedDataFor("spy", start="2019-01-01", end="2020-01-01")
print(spy)
