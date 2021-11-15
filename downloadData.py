import yfinance as yf
from yahoofinancials import YahooFinancials
from pricePoint import PricePoint


def getFormattedDataFor(ticker, start=None, end=None):
    return formatDataAsPricePoint(downloadDataFor(ticker, start, end))


def downloadDataFor(ticker, start=None, end=None):
    if start is None or end is None:
        return yf.download(ticker)
    else:
        return yf.download(ticker, start=start, end=end, interval="1d")


# Returns data from yFinance as an array of PricePoint objects
def formatDataAsPricePoint(data):
    formattedData = []
    data.reset_index(inplace=True)

    for index, close in enumerate(data['Close']):
        date = (data['Date'][index]).strftime("%x")

        if close is not None and date is not None:
            formattedData.append(PricePoint(close, date))

    return formattedData


# COMMODITY AND CURRENCY
def getFormattedDataForCommodity(currency, start=None, end=None):
    return formatDataAsPricePointForCommodity(currency, downloadDataForCommodity(currency, start, end))


def downloadDataForCommodity(currency, start=None, end=None):
    currencies = YahooFinancials([currency])

    if start is None or end is None:
        return currencies.get_historical_price_data()
    else:
        return currencies.get_historical_price_data(start, end, "daily")


def formatDataAsPricePointForCommodity(currency, data):
    formattedData = []
    prices = data[list(data.keys())[0]]['prices']

    for price in prices:
        close = price['close']
        date = price['formatted_date']

        if close is not None and date is not None:
            formattedData.append(PricePoint(close, date))

    return formattedData