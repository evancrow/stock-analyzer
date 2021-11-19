import PySimpleGUI as sg
import yfinance as yf

sg.theme('DarkAmber')  # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Enter A Stock Ticker'), sg.InputText()],
          [sg.Button('Ok'), sg.Button('Cancel')]]

# Create the Window
window = sg.Window('Stock Predictor', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Ok':  # if user closes window or clicks any button
        break

ticker = str(values[0])

stockData = yf.download(ticker, start="2017-01-01", end="2017-04-30")

print(ticker)
print(stockData)

window.close()
