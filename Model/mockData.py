import downloadData
from Model.pattern import Pattern
from Model.mockDataType import MockData


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
    return MockData(type=Pattern.bearishHeadAndShoulders,
                    data=downloadData.getFormattedDataForCommodity('USDJPY=x', start="1997-04-30", end="1997-07-30"))


def BEARISH_RISING_WEDGE():
    return MockData(type=Pattern.bearishRisingWedge,
                    data=downloadData.getFormattedDataForCommodity('USDJPY=x', start="2020-03-20", end="2020-03-28"))


def BULLISH_DOUBLE_BOTTOM():
    return MockData(type=Pattern.bullishDoubleBottom,
                    data=downloadData.getFormattedDataFor('VOD', start="2018-10-15", end="2018-11-13"))


def BULLISH_INVERTED_HEAD_AND_SHOULDERS():
    return MockData(type=Pattern.bullishInvertedHeadAndShoulders,
                    data=downloadData.getFormattedDataForCommodity('SM', start="1996-10-30", end="1997-01-10"))


def BULLISH_FALLING_WEDGE():
    return MockData(type=Pattern.bullishFallingWedge,
                    data=downloadData.getFormattedDataForCommodity('DX', start="1997-10-22", end="1997-11-20"))


def formatData(stocks):
    maximumDataLength = len(stocks[0].data)

    # find the stock with the least amount of data
    for stock in stocks:
        print(stock.name, len(stock.data))
        if len(stock.data) < maximumDataLength:
            maximumDataLength = len(stock.data)

    # make sure no stocks exceed the maximum length
    for i in range(len(stocks)):
        data = []

        for ii in range(len(stocks[i].data)):
            if ii < maximumDataLength:
                data.append(stocks[i].data[ii])

        stocks[i] = data

    return stocks



def mockDataForPattern(pattern):
    if pattern == Pattern.bearishDoubleTop:
        return formatData(BEARISH_DOUBLE_TOP_MOCK_DATA())
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