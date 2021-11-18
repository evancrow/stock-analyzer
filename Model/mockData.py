import downloadData
from Model.pattern import Pattern
from Model.mockDataType import MockData
import arrayHelper


def BEARISH_DOUBLE_TOP_MOCK_DATA():
    return [
        MockData(name="nflx",
                 type=Pattern.bearishDoubleTop,
                 data=downloadData.getFormattedDataFor('nflx', start="2018-02-20", end="2018-05-01")),
        MockData(name="amzn",
                 type=Pattern.bearishDoubleTop,
                 data=downloadData.getFormattedDataFor('amzn', start="2018-09-1", end="2018-11-1"))
    ]


def BEARISH_HEAD_AND_SHOULDERS():
    return [
        MockData(type=Pattern.bearishHeadAndShoulders,
                 data=downloadData.getFormattedDataForCommodity('USDJPY=x', start="1997-04-30", end="1997-07-30"))
    ]


def BEARISH_RISING_WEDGE():
    return [
        MockData(type=Pattern.bearishRisingWedge,
                 data=downloadData.getFormattedDataForCommodity('USDJPY=x', start="2020-03-20", end="2020-03-28"))
    ]


def BULLISH_DOUBLE_BOTTOM():
    return [
        MockData(type=Pattern.bullishDoubleBottom,
                 data=downloadData.getFormattedDataFor('VOD', start="2018-10-15", end="2018-11-13"))
    ]


def BULLISH_INVERTED_HEAD_AND_SHOULDERS():
    return [
        MockData(type=Pattern.bullishInvertedHeadAndShoulders,
                 data=downloadData.getFormattedDataForCommodity('SM', start="1996-10-30", end="1997-01-10"))
    ]


def BULLISH_PENNANT():
    return [
        MockData(type=Pattern.bullishPennant,
                 data=downloadData.getFormattedDataFor('IO', start="2019-01-07", end="2019-02-12"))
    ]


def formatData(stocks):
    data = []

    for stock in stocks:
        data.append(stock.data)

    formatedData = arrayHelper.equalArrayLengths(data)

    for i in range(len(data)):
        stocks[i].data = formatedData[i]

    return stocks


def mockDataForPattern(pattern):
    if pattern == Pattern.bearishDoubleTop:
        return formatData(BEARISH_DOUBLE_TOP_MOCK_DATA())
    elif pattern == Pattern.bearishHeadAndShoulders:
        return formatData(BEARISH_HEAD_AND_SHOULDERS())
    elif pattern == Pattern.bearishRisingWedge:
        return formatData(BEARISH_RISING_WEDGE())
    elif pattern == Pattern.bullishDoubleBottom:
        return formatData(BULLISH_DOUBLE_BOTTOM())
    elif pattern == Pattern.bullishInvertedHeadAndShoulders:
        return formatData(BULLISH_INVERTED_HEAD_AND_SHOULDERS())
    elif pattern == Pattern.bullishPennant:
        return formatData(BULLISH_PENNANT())
