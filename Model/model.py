from sklearn.linear_model import LinearRegression
from Model import mockData
from Model.pattern import Pattern

trainInput = list()
trainOutput = list()

for pattern in Pattern:
    patternData = mockData.mockDataForPattern(pattern)
    trainInput.append(patternData.data)
    trainOutput.append(patternData.type)

print(trainInput, trainOutput)
