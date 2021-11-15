import math
from neuralNet import NeuralNetwork
from Model import mockData
from Model.pattern import Pattern
import numpy as np
from predection import Predection


def pricePointToMatriceData(data):
    prices = []
    max = 0

    for point in data:
        price = point.price
        if price > max:
            max = math.ceil(price)
        prices.append(price or 0)

    # Divide all number by ten to the number of ten places in the highest number
    divisible = math.pow(10, len(str(max)[::-1]))

    for i in range(len(prices)):
        prices[i] = prices[i] / divisible

    return prices


def convertToNeuralNetData(data):
    stockPrices = []

    for stock in data:
        prices = pricePointToMatriceData(stock.data)
        stockPrices.append(prices)

    stockPrices = np.array(stockPrices, dtype=float)
    return stockPrices


def neuralNetForPattern(pattern):
    trainOutput = []

    patternData = mockData.mockDataForPattern(pattern)
    trainInput = convertToNeuralNetData(patternData)

    for i in range(len(patternData)):
        trainOutput.append(pattern.value)

    trainInput = np.array(trainInput)
    trainInput.reshape(-1, 1)

    trainOutput = np.array([trainOutput]).T

    # number of weights must match number of inputs
    numberOfWeights = len(trainInput[0])

    neuralNet = NeuralNetwork(pattern, trainInput, trainOutput, numberOfWeights)
    neuralNet.train()

    return neuralNet


def createNeuralNets():
    neuralNets = []

    for pattern in Pattern:
        neuralNets.append(neuralNetForPattern(pattern))

    return neuralNets


def identifyPatternsFor(data):
    neuralNets = createNeuralNets()
    matchingPatterns = []

    for net in neuralNets:
        predectionValue = net.predict(pricePointToMatriceData(data))
        error = abs(net.pattern.value - predectionValue)

        if error < 0.0004:
            matchingPatterns.append(net.pattern)

    return matchingPatterns


# Example call: priceMovementPredictionFor(mockData.mockDataForPattern(Pattern.bearishDoubleTop)[0].data)
def priceMovementPredictionFor(data):
    matchingPatterns = identifyPatternsFor(data)
    bullish = []
    bearish = []

    for pattern in matchingPatterns:
        if pattern.value < 0.3:
            bearish.append(pattern)
        else:
            bullish.append(pattern)

    if len(bullish) > len(bearish):
        return Predection.bullish
    elif len(bullish) < len(bearish):
        return Predection.bearish
    else:
        return Predection.none


print(priceMovementPredictionFor(mockData.mockDataForPattern(Pattern.bearishDoubleTop)[0].data))
