import math
import pickle
import numpy as np
from Model import mockData
from Model.pattern import Pattern
from arrayHelper import equalArrayLengths


class NeuralNetwork():
    def __init__(self, pattern, inputs, outputs, numberOfWeights=0, weights=None, error_history=None, epoch_list=None):
        self.pattern = pattern
        self.inputs = inputs
        self.outputs = outputs

        if weights is None:
            # initialize weights as .50 for simplicity
            placeholderWeights = []
            for i in range(numberOfWeights):
                placeholderWeights.append([.50])

            self.weights = np.array(placeholderWeights)
        else:
            self.weights = weights

        if error_history is not None:
            self.error_history = error_history
        else:
            self.error_history = []

        if epoch_list is not None:
            self.epoch_list = epoch_list
        else:
            self.epoch_list = []

    def getSerializedData(self):
        return {
            'Pattern': self.pattern.value,
            'Inputs': self.inputs,
            'Outputs': self.outputs,
            'Weights': self.weights,
            'Error_history': self.error_history,
            'Epoch_list': self.epoch_list
        }

    # activation function ==> S(x) = 1/1+e^(-x)
    def sigmoid(self, x, deriv=False):
        if deriv == True:
            return x * (1 - x)

        return 1 / (1 + np.exp(-x))

    # data will flow through the neural network.
    def feed_forward(self):
        self.hidden = self.sigmoid(np.dot(self.inputs, self.weights))

    # going backwards through the network to update weights
    def backpropagation(self):
        self.error = self.outputs - self.hidden
        delta = self.error * self.sigmoid(self.hidden, deriv=True)
        self.weights += np.dot(self.inputs.T, delta)

    # Epochs is the number of times the model is run
    def train(self, epochs=10000):
        for epoch in range(epochs):
            # flow forward and produce an output
            self.feed_forward()
            # go back though the network to make corrections based on the output
            self.backpropagation()
            # keep track of the error history over each epoch
            self.error_history.append(np.average(np.abs(self.error)))
            self.epoch_list.append(epoch)

    # function to predict output on new and unseen input data
    def predict(self, new_input):
        adjustedArrays = equalArrayLengths([new_input, self.weights])
        adjusted_new_input = adjustedArrays[0]
        adjusted_weights = adjustedArrays[1]

        prediction = self.sigmoid(np.dot(adjusted_new_input, adjusted_weights))
        return prediction


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

    persistNeuralNets(neuralNets)

    return neuralNets


def persistNeuralNets(neuralNets):
    formattedNets = []

    for neuralNet in neuralNets:
        formattedNets.append(neuralNet.getSerializedData())

    picklefile = open('neuralNets.pkl', 'wb')
    pickle.dump(formattedNets, picklefile)
    picklefile.close()


def retrieveNeuralNets():
    picklefile = open('neuralNets.pkl', 'rb')
    serializedNets = pickle.load(picklefile)
    picklefile.close()

    neuralNets = []

    for serializedNet in serializedNets:
        neuralNets.append(
            NeuralNetwork(Pattern(serializedNet['Pattern']), serializedNet['Inputs'], serializedNet['Outputs'],
                          weights=serializedNet['Weights'], error_history=serializedNet['Error_history'],
                          epoch_list=serializedNet['Epoch_list']))

    return neuralNets


createNeuralNets()
