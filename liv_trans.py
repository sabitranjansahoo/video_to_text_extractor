import speech_recognition as sr
import  PySimpleGUI as sg
import pyaudio
r = sr.Recognizer()
m = sr.Microphone()

layout = [[sg.Text('Live Speech To Text', font='Helvetica 15')],
          [sg.ReadButton('Speak'), sg.ReadButton('Stop')],
          [sg.Output(size=(80, 10))],
          [sg.Exit()]]

window = sg.Window('Text Extractor').Layout(layout)

while True:
    event,values = window.Read()
    if event is None or event == 'Exit':
        break
    elif event == 'Speak':
        with m as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            value = r.recognize_google(audio, language="en-US")
            print(value)

window.Close()
