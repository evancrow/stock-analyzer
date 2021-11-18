import downloadData
from Model import mockData
from Model.pattern import Pattern
from prediction import Prediction
import neuralNet


def identifyPatternsFor(data):
    neuralNets = neuralNet.retrieveNeuralNets()
    matchingPatterns = []

    for net in neuralNets:
        predectionValue = net.predict(neuralNet.pricePointToMatriceData(data))
        error = abs(net.pattern.value - predectionValue)
        print(net.pattern, error)

        if error < 0.05:
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
        return Prediction.bullish
    elif len(bullish) < len(bearish):
        return Prediction.bearish
    else:
        return Prediction.none


print(priceMovementPredictionFor(downloadData.getFormattedDataFor('SPY', start='2021-11-1', end='2021-11-18')))
