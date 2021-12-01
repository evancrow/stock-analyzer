import pylab
from enum import Enum
import plotly.graph_objects as go


class Column(Enum):
    open = 'Open'
    close = 'Close'
    high = 'High'
    low = 'Low'
    candlestick = 'Candlestick'


def graphAllData(data):
    data.plot(subplots=True)
    pylab.show()


def graphData(data, type: Column):
    if type.value == 'candlestick' :
        fig = go.Figure(data=[go.Candlestick(
            open=data['Open'],
            high=data['High'],
            low=data['Low'],
            close=data['Close'])])

        fig.show()
    else:
        data.plot(y=type.value)
        pylab.show()


