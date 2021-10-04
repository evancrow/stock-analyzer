import downloadData
from Model.model import Pattern

class MockData:
    def __init__(self, type, data):
        self.type = type
        self.data = data

def BEARISH_DOUBLE_TOP_MOCK_DATA():
    return MockData(Pattern.bearishDoubleTop, downloadData.getFormattedDataFor('nflx', start="2018-02-20", end="2018-05-01"))

def BEARISH_HEAD_AND_SHOULDERS():
    return MockData(Pattern.bearishHeadAndShoulders, [0, 1, 2])

def BEARISH_RISING_WEDGE():
    return MockData(Pattern.bearishRisingWedge, [0, 1, 2])

def BULLISH_DOUBLE_BOTTOM():
    return MockData(Pattern.bullishDoubleBottom, [0, 1, 2])

def BULLISH_INVERTED_HEAD_AND_SHOULDERS():
    return MockData(Pattern.bullishInvertedHeadAndShoulders, [0, 1, 2])

def BULLISH_FALLING_WEDGE():
    return MockData(Pattern.bullishFallingWedge, [0, 1, 2])
