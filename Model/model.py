import math
from neuralNet import NeuralNetwork
from Model import mockData
from Model.pattern import Pattern
import numpy as np


def convertToNerualNetData(data):
    stockPrices = []

    for stock in data:
        prices = []
        max = 0

        for point in stock:
            price = point.price
            if price > max:
                max = math.ceil(price)
            prices.append(price or 0)

        # Divide all number by ten to the number of ten places in the highest number
        divisible = math.pow(10, len(str(max)[::-1]))

        for i in range(len(prices)):
            prices[i] = prices[i] / divisible

        stockPrices.append(prices)

    stockPrices = np.array(stockPrices, dtype=float)
    return stockPrices


def neuralNetForPattern(pattern):
    trainOutput = []

    patternData = mockData.mockDataForPattern(pattern)
    trainInput = convertToNerualNetData(patternData)

    for i in range(len(patternData)):
        trainOutput.append(pattern.value)

    trainInput = np.array(trainInput)
    trainInput.reshape(-1, 1)

    trainOutput = np.array([trainOutput]).T

    # number of weights must match number of inputs
    numberOfWeights = len(trainInput[0])

    neuralNet = NeuralNetwork(trainInput, trainOutput, numberOfWeights)
    neuralNet.train()

    return neuralNet