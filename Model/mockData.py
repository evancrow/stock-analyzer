from enum import Enum
from Model.model import Pattern
from pricePoint import PricePoint
import yfinance as yf

class MockData:
    def __init__(self, type, data):
        self.type = type
        self.data = data

    bearishDoubleTop = "Bearish Double Top"
    bearishHeadAndShoulders = "Bearish Head And Shoulders"
    bearishRisingWedge = "Bearish Rising Wedge"
    bullishDoubleBottom = "Bullish Double Bottom"
    bullishInvertedHeadAndShoulders = "Bullish Inverted Head And Shoulders"
    bullishFallingWedge = "Bullish Falling Wedge"

def BEARISH_DOUBLE_TOP_MOCK_DATA():
    return MockData(Pattern.bearishDoubleTop, [PricePoint(), 1, 2])

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

