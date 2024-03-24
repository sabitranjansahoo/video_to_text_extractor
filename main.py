import PySimpleGUI as sg


layout=[[sg.Text("Text Extractor" , font ="Helvetica 15")],
[sg.ReadButton('Video to Text'),sg.ReadButton("Live Speech To Text")],
[sg.Exit()]]

window= sg.Window('TEXT EXTRACTOR').Layout(layout)
while True:
    event,values = window.Read()
    if event is'Exit':
        break
    elif event == 'Live Speech To Text':
        import liv_trans
        run('liv_trans.py')
    elif event == 'Video to Text':
        import vid_to_text
        run('vid_to_text.py')
            
            
window.close()
