from neuralNet import NeuralNetwork
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

    trainInput = np.array(trainInput)
    trainInput.reshape(-1, 1)

    trainOutput = np.array([trainOutput]).T

    # number of weights must match number of inputs
    numberOfWeights = len(trainInput[0])

    neuralNet = NeuralNetwork(trainInput, trainOutput, numberOfWeights)
    neuralNet.train()

    return neuralNet
