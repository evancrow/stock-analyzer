import PySimpleGUI as sg
from Model import predections

sg.theme('LightGrey1')


def open(prediction):
    text = "No predicition available ☹️"
    if prediction == predections.Prediction.bullish:
        text = "The stock will go up!"
    elif prediction == predections.Prediction.bearish:
        text = "The stock will go down!"

    layout = [[sg.Text(text, font=('Any 18'))],
              [sg.Button('Restart')]]
    window = sg.Window('Security Prediction', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            window.close()
            return False
        elif event == 'Restart':
            window.close()
            return True