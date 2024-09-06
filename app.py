import pyttsx3
from tkinter import *
import os
import speech_recognition
from tkinter import filedialog


win = Tk()
win.minsize(240, 50)
win.maxsize(240, 50)
win.configure(bg="black")
win.resizable(False, False)
cv_text_voice_btn = Button(
    win, text="Convert text to voice", command=lambda: text_to_voice()
).grid(row=0, column=0, columnspan=3)
cv_voice_text_btn = Button(
    win, text="Convert voice to text", command=lambda: voice_to_text()
).grid(row=0, column=3)


def text_to_voice():
    tv = Toplevel(win)
    tv.title("text to voice")
    tv.configure(bg="#75CEFF")
    tv.minsize(500, 300)
    tv.maxsize(500, 300)
    
    text_entry = Entry(tv, bd=10, fg="black", font=("arial", "20", "bold"))
    text_entry.grid(row=0, column=2, columnspan=4)

    text_label = Label(tv, text="text:", font=("arial", "20", "bold"))
    text_label.grid(row=0, column=0)
    
    filename_entry = Entry(tv, bd=10, fg="black", font=("arial", "20", "bold"))
    filename_entry.grid(row=2, column=2, columnspan=5)

    filename_label = Label(tv, text="filename:", font=("arial", "20", "bold"))
    filename_label.grid(row=2, column=0)
    
    submit_button=Button(tv, text="submit", font=("arial", "20", "bold"),command=lambda:convert_and_save())
    submit_button.grid(row=3,column=4,pady=50)
    play_button = Button(tv, text="play", font=("arial", "20", "bold"),command=lambda:open())
    play_button.grid(row=3, column=3,  pady=50)
    
    
    def convert_and_save():
        text=text_entry.get()
        global filename
        filename=filename_entry.get()
        engine = pyttsx3.init()
        voices = engine.getProperty("voices")
        rate = engine.getProperty("rate")
        engine.setProperty("rate", 125)
        engine.setProperty("voice", voices[0].id)#user choice 1 or 0
        # engine.say(n)
        engine.save_to_file(text , f'{filename}.wav')
        engine.runAndWait() 
        open()
        
    def open():
        filename = filename_entry.get()
        if f"{filename}.wav" in os.listdir():
            os.system(f"start {filename}.wav")
    tv.mainloop()


def voice_to_text():
    vt = Toplevel(win)
    vt.title("text to voice")
    vt.configure(bg="#0CC75E")

    vt.minsize(700, 500)
    vt.maxsize(700, 500)

    filename_entry = Entry(vt, bd=10, fg="black", font=("arial", "20", "bold"))
    filename_entry.grid(row=0, column=2, columnspan=4)

    filename_label = Label(vt, text="filename:", font=("arial", "20", "bold"))
    filename_label.grid(row=0, column=0, pady=(10, 10))
    
   
    submit_button = Button(
        vt, text="submit", font=("arial", "20", "bold"), command=lambda:  voice_totext()
    )
    submit_button.grid(row=1, column=2, padx=40, pady=(10, 10))
    
    # submit_btn = Button(
    #     vt, text="submit", font=("arial", "20", "bold",), command=lambda:  voice_totext()

    # )
    # submit_btn.grid(row=4, column=2, padx=0, pady=(10, 10))

    Transcription=Label(vt,text='',font=("arial", "12", "",),wraplength=400, justify=LEFT,bg='#0CC75E',fg='black')
    Transcription.grid(row=2,column=0,columnspan=4, padx=10,pady=(10, 10))
    
    
    
    def voice_totext():
        # filename=filename_entry.get()
        filename= filedialog.askopenfilename(
        title="Select an MP3 File",
        filetypes=[("wav files", "*.wav"), ("All files", "*.*")])

        srr=speech_recognition.Recognizer()
        with speech_recognition.AudioFile(filename) as source:
            audio_data = srr.record(source)
        try:
        # Recognize speech using Sphinx (offline)
            text = srr.recognize_sphinx(audio_data)
            Transcription.config(text=text)
            # print("Transcription: ", text)
            return text
        except  Exception as e:
            print('error')
   


    
    vt.mainloop()


win.mainloop()
