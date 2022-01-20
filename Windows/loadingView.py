import PySimpleGUI as sg
sg.theme('LightGrey1')

layout = [[sg.Text('Predecting... 🤔', key='loadingText')]]

def open():
    window = sg.Window('Predicting', layout)
    return window