from sklearn.linear_model import LinearRegression
from Model import mockData
from Model.pattern import Pattern
import numpy as np

def getAllPrices(data):
    prices = []

    for point in data:
        prices.append(point.price or 0)

    prices = np.array(prices, dtype=float)
    return prices

def modelForPattern(pattern):
    trainInput = []
    trainOutput = []

    patternData = mockData.mockDataForPattern(pattern)
    trainInput.append(getAllPrices(patternData.data))
    trainOutput.append(patternData.type.value)

    trainInput = np.array(trainInput, dtype=object)
    trainInput.reshape(-1, 1)

    predictor = LinearRegression()
    predictor.fit(trainInput, trainOutput)

    return predictor

modelForPattern(Pattern.bearishDoubleTop)