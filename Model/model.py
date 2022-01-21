from Model.predections import Prediction
from Model import neuralNet


def identifyPatternsFor(data):
    neuralNets = neuralNet.retrieveNeuralNets()
    matchingPatterns = []

    for net in neuralNets:
        predictionValue = net.predict(neuralNet.pricePointToMatriceData(data))
        error = abs(net.pattern.value - predictionValue)
        print(net.pattern, error)

        if error < 0.05:
            matchingPatterns.append(net.pattern)

    return matchingPatterns


# Example call: priceMovementPredictionFor(downloadData.getFormattedDataFor('AAPL', start='2021-11-1',
# end='2021-11-18')))
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