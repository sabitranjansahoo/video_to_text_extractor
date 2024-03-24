from tkinter.constants import BROWSE
from typing import Any
from PySimpleGUI.PySimpleGUI import FileBrowse, ReadButton
import moviepy.editor as mp
import speech_recognition
import PySimpleGUI as sg
import pyaudio
layout = [[sg.Text("Video To Text",font = 'Helvetica 15')],[sg.ReadButton('Browse')],[sg.Output(size=(80,10))],[sg.Exit()]]
window= sg.Window('Text Extractor').Layout(layout)

while True:
    event,value = window.Read()
    if event == 'Exit':
        break
    elif event == 'Browse':
        import os
        import speech_recognition as sr
        import tkinter
        from tkinter.filedialog import askopenfilename
        r = sr.Recognizer()
        clip = mp.VideoFileClip(askopenfilename()) 
        audio = clip.audio
        audio.write_audiofile('converted.wav')
        r = sr.Recognizer()
        audio = sr.AudioFile('converted.wav')
        with audio as source:
            audio_file = r.record(source)
        result = r.recognize_google(audio_file)
        with open('recognized.txt',mode ='w') as file: 
          file.write("Recognized Speech:") 
          file.write("\n") 
          file.write(result) 
        print("ready!")
        os.system('gedit recognized.txt')
        break
        





window.close()