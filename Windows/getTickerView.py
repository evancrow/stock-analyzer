import PySimpleGUI as sg

sg.theme('LightGrey1')

def createWindow():
    # All the stuff inside your window.
    layout = [[sg.Text('Enter a ticker:', key='actionText'), sg.InputText()],
              [sg.Checkbox('Security is a commodity/currency', default=False, key="isCommodity")],
              [sg.Button('Predict 🧠')]]

    return sg.Window('Stock Predictor', layout)


def open():
    window = createWindow()

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            window.close()
            break
        elif event == 'Predict 🧠':
            ticker = str(values[0])

            if not ticker:
                window['actionText'].update('Enter a ticker: (required)')
            else:
                window.close()
                return ticker, values["isCommodity"]