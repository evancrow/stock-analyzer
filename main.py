import downloadData
from Model import model
from Windows import getTickerView
from Windows import loadingView
from Windows import predictionView


def startApp():
    ticker, isCommodity = getTickerView.open()
    dates = downloadData.getDateAndThirtyDaysAgo()

    if isCommodity == False:
        stockData = downloadData.getFormattedDataFor(ticker, start=dates[1], end=dates[0])
    else:
        stockData = downloadData.getFormattedDataForCommodity(ticker, start=dates[1], end=dates[0])

    prediction = model.priceMovementPredictionFor(stockData)

    if predictionView.open(prediction):
        startApp()


startApp()
