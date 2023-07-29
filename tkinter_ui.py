from tkinter import *
from tkinter.filedialog import askopenfilename
import moviepy.editor as me

import helper
from constants import AUDIO_FILE_NAME

root = Tk()
summary = ''
def convert():
    global filename
    global summary

    video = me.VideoFileClip(filename)

    # Extract the Audio
    audio = video.audio

    audio.write_audiofile(AUDIO_FILE_NAME)
    summary = helper.convert_and_generate_summary()
    final = summary.split('.')
    final_summary = '\n'.join(final)

    # Create a label to display text summary
    label3.config(text=final_summary, fg="green", font=("Footlight MT", 10 ,"bold"),justify=LEFT)
    label3.place(x=300, y=450)
    label3.config(bg="white")
    return

def select():
    global filename
    filetypes = (
        ('video files',
         '*.WEBM , *.MPG, *.MP2 , *.MPEG , *.MPE , *.MPV , *.MP4 , *.M4P , *.M4V , *.AVI , *.WMV , *.MOV , *.QT , *.FLV , *.SWF , *.AVCHD'),
        ('All files', '*.*')
    )
    filename = askopenfilename(filetypes=filetypes)
    # Create a label to display video selected
    label3.config(text="Video Selected", fg="green")
    label3.config(bg="white")
    # format.set(".wav")

    # Create a button to convert video to audio
    button3 = Button(root, text="Proceed", bg='light blue', font=("Harlow Solid", 12), command=convert, width=10,
                     height=1)
    button3.pack()
    button3.place(x=700, y=300)
    return

def create_ui():
    global label3
    # Create the basic GUI window
    # Set the background color of GUI application
    root.configure(bg='white')

    # Set the geometry of the GUI application
    root.geometry("700x450")
    root.minsize(1500, 1000)

    root.maxsize(600, 350)

    # Set the title of the GUI application
    root.title("Video to Audio Converter")

    # Create a label for heading
    label1 = Label(root, text="Video Summarization", font=("Arial", 32))
    label1.config(bg="white")
    label1.pack()

    # Create a label to display Select any Video file
    label2 = Label(root, text="Select any Video file", font=("Arial", 18))
    label2.config(bg="white")
    label2.pack()
    label2.place(x=630, y=100)

    # Create a button for choosing video
    button1 = Button(root, text="Choose file", bg='light blue', font=("Harlow Solid", 12), command=select, width=10,
                     height=1)
    button1.pack()
    button1.place(x=700, y=200)
    label3 = Label(root, font=("Footlight MT", 18, "bold"))
    label3.pack()
    label3.place(x=660, y=150)


    format = StringVar()
    # Start the GUI application
    root.mainloop()