import PySimpleGUI as sg
import yfinance as yf
from model import priceMovementPredictionFor

import downloadData

sg.theme('DarkAmber')  # Add a touch of color
# All the stuff inside your window.
layout1 = [[sg.Text('Enter A Stock Ticker'), sg.InputText()],
           [sg.Button('Ok'), sg.Button('Cancel')]]

# Create the Window
window = sg.Window('Stock Predictor', layout1, size=(225, 100))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == 'Ok':  # if user closes window or clicks any button
        ticker = str(values[0])
        prediction = priceMovementPredictionFor(downloadData.getFormattedDataFor(ticker, start='2021-11-1', end='2021-11-18'))
        layout1 = [[sg.Text(prediction)]]
        window.close()
        window = sg.Window('Stock Predictor', layout1, size=(225, 100))
    if event == sg.WIN_CLOSED or event == 'Cancel':
        window.close()
        break

# layout2 = [[sg.Text(
#    priceMovementPredictionFor(downloadData.getFormattedDataFor(ticker, start='2021-11-1', end='2021-11-18')))]]
# window2 = sg.Window('Stock Predictor', layout2)

# while True:
#    event, values = window2.read()
#    if event == sg.WIN_CLOSED:
#        window2.close()
#        break
# print(ticker)
# print(stockData)
# window.close()
