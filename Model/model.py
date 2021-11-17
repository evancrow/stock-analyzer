from Model import mockData
from Model.pattern import Pattern
from predection import Predection
import neuralNet


def identifyPatternsFor(data):
    neuralNets = neuralNet.retrieveNeuralNets()
    matchingPatterns = []

    for net in neuralNets:
        predectionValue = net.predict(neuralNet.pricePointToMatriceData(data))
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
