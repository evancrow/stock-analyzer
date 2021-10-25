import matplotlib.pyplot as plt
import downloadData
import pylab
import pandas as pd
data = pd.DataFrame(downloadData.downloadDataFor('SPY'))
#needs a dataFrame
def graphDataAll(data = pd.DataFrame()):
    data.plot(subplots=True, )
    pylab.show()

def graphDataOpen(data = pd.DataFrame()):
    data.plot(y='Open')
    pylab.show()

def graphDataHigh(data = pd.DataFrame()):
    data.plot(y='High')
    pylab.show()

def graphDataLow(data = pd.DataFrame()):
    data.plot(y='Low')
    pylab.show()

def graphDataClose(data = pd.DataFrame()):
    data.plot(y='Close')
    pylab.show()

graphDataAll(data)
graphDataOpen(data)
graphDataClose(data)
graphDataHigh(data)
graphDataLow(data)
