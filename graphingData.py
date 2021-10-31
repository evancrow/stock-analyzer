import matplotlib.pyplot as plt
import downloadData
import pylab
import pandas as pd
from enum import Enum


class Column(Enum):
    open = 'Open'
    close = 'Close'
    high = 'High'
    low = 'Low'


def graphAllData(data):
    data.plot(subplots=True)
    pylab.show()


def graphData(data, type: Column):
    data.plot(y=type.value)
    pylab.show()
