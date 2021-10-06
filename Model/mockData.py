import downloadData
from Model.pattern import Pattern
from Model.mockDataType import MockData


def BEARISH_DOUBLE_TOP_MOCK_DATA():
    return MockData(Pattern.bearishDoubleTop,
                    downloadData.getFormattedDataFor('nflx', start="2018-02-20", end="2018-05-01"))


def BEARISH_HEAD_AND_SHOULDERS():
    return MockData(Pattern.bearishHeadAndShoulders,
                    downloadData.getFormattedDataForCommodity('USDJPY=x', start="1997-04-30", end="1997-07-30"))


def BEARISH_RISING_WEDGE():
    return MockData(Pattern.bearishRisingWedge,
                    downloadData.getFormattedDataForCommodity('USDJPY=x', start="2020-03-20", end="2020-03-28"))


def BULLISH_DOUBLE_BOTTOM():
    return MockData(Pattern.bullishDoubleBottom,
                    downloadData.getFormattedDataFor('VOD', start="2018-10-15", end="2018-11-13"))


def BULLISH_INVERTED_HEAD_AND_SHOULDERS():
    return MockData(Pattern.bullishInvertedHeadAndShoulders,
                    downloadData.getFormattedDataForCommodity('PB', start="1995-12-22", end="1996-02-16"))


def BULLISH_FALLING_WEDGE():
    return MockData(Pattern.bullishFallingWedge,
                    downloadData.getFormattedDataForCommodity('DX', start="1997-10-22", end="1997-11-20"))


def mockDataForPattern(pattern):
    if pattern == Pattern.bearishDoubleTop:
        return BEARISH_DOUBLE_TOP_MOCK_DATA()
    elif pattern == Pattern.bearishHeadAndShoulders:
        return BEARISH_HEAD_AND_SHOULDERS()
    elif pattern == Pattern.bearishRisingWedge:
        return BEARISH_RISING_WEDGE()
    elif pattern == Pattern.bullishDoubleBottom:
        return BULLISH_DOUBLE_BOTTOM()
    elif pattern == Pattern.bullishInvertedHeadAndShoulders:
        return BULLISH_INVERTED_HEAD_AND_SHOULDERS()
    elif pattern == Pattern.bullishFallingWedge:
        return BULLISH_FALLING_WEDGE()
