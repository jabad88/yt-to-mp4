from pytube import YouTube
from tkinter import *
from tkinter import messagebox

#-----------------------Converter-----------------------#
def convert():
    link = link_box.get()
    yt = YouTube(link)
    title = yt.title
    author = yt.author

    confirm = messagebox.askyesno(message=f"Download? \nTITLE: {title}\nCHANNEL: {author}")

    if confirm == True:
        final_dl = (yt.streams.get_audio_only())
        final_dl.download(output_path='~/Downloads')
        messagebox.showinfo("Download complete!!:)")


#-----------------------GUI-----------------------#

window=Tk()
window.title("YouTube to MP4 Downloader")
window.geometry("500x500")

title = Label(text="Youtube to MP4 Converter", font=("Aerial", 20, 'bold'))
title.pack()

ask_for_link = Label(text="Please provide the link to the video: ", font=("Aerial", 15))
ask_for_link.pack()

link_box = Entry(width=36)
link_box.pack()

button = Button(text="Convert", width=20, command=convert)
button.pack()


window.mainloop()