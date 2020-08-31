import wolframalpha

client = wolframalpha.Client("JJEL8R-WYHXEX2EQL")

import wikipedia

'''
want this to pop up on a window 
'''
import PySimpleGUI as sg

sg.theme('LightPurple')
# All the stuff inside your window.
layout = [[sg.Text('Enter a command'), sg.InputText()],
          [sg.Button('Ok'), sg.Button('Cancel')]]

# Create the Window
window = sg.Window('Your AI', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    # res = client.query(values[0])  # holds the question the user asks from wolfram
    # wolfram_res = next(res.results).text

    res = client.query(values[0])  # holds the question the user asks from wolfram
    wolfram_res = next(res.results).text
    wiki_res = wikipedia.summary(values[0], sentences=2)
    sg.Popup(values[0], "Wolfram Result: " + wolfram_res,
             "Wikipedia Result: " + wiki_res)  # opens answer in another window

window.close()
