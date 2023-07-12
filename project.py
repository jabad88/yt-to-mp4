"""
Youtube to MP4 Converter
Student: Joshua Maturan Abadies
Location: California, USA
GitHub: https://github.com/jabad88

"""


from pytube import YouTube
from tkinter import *
from tkinter import messagebox
import re
import csv
import os

def main():
    link = link_box.get()
    valid_link = check_valid_link(link)
    final_dl = convert(valid_link)
    if final_dl == True:
        get_csv(link)

#-----------------------Converter-----------------------#
def convert(link):
    yt = YouTube(link)
    title = yt.title
    author = yt.author

    confirm = messagebox.askyesno(message=f"Download? \nTITLE: {title}\nCHANNEL: {author}")

    if confirm == True:
        (yt.streams.filter(only_audio=True).first().download(output_path="Pytube Downloader"))
        messagebox.showinfo(message="Download complete!!:)")
        link_box.delete(0,END)
        return True

#-----------------------Check Youtube Link-----------------------#

def check_valid_link(link):
    if re.search(r"(?:https?:\/\/)?(?:www\.)?youtu(?:\.be\/|be.com\/\S*(?:watch|embed)(?:(?:(?=\/[-a-zA-Z0-9_]{11,}(?!\S))\/)|(?:\S*v=|v\/)))([-a-zA-Z0-9_]{11,})",link):
        return link
    else:
        (messagebox.showerror(message="Not a Valid Youtube Link."))
        link_box.delete(0,END)

#-----------------------Add to CSV-----------------------#
def get_csv(link):
    yt = YouTube(link)
    if not (os.path.isfile("prev_download.csv")):
        with open("prev_download.csv", "a") as f:
            prev_dl = csv.DictWriter(f, fieldnames=["title","channel","link"])
            prev_dl.writeheader()
            prev_dl.writerow({"title":yt.title, "channel":yt.author,"link":link})
            return "successfully written to csv"
    else:
        with open("prev_download.csv", "a") as f:
            prev_dl = csv.DictWriter(f, fieldnames=["title","channel","link"])
            prev_dl.writerow({"title":yt.title, "channel":yt.author,"link":link})
            return "successfully written to csv"

#-----------------------GUI-----------------------#
window=Tk()
window.title("YouTube to MP4 Downloader")
window.geometry("500x350")
window.configure(bg="white")

title = Label(text="Youtube to MP4 Converter", font=("Aerial", 35, 'bold'),bg="white",fg="black",padx=30,pady=30)
title.grid(row=1,column=0)

ask_for_link = Label(text="Please provide the link to the video: ", font=("Aerial", 20),bg="white",fg="black",padx=30)
ask_for_link.grid(row=2,column=0)

link_box = Entry(width=36, bg="white",fg="black",highlightbackground="grey")
link_box.grid(row=3,column=0)

button = Button(text="Convert", width=20, command=main, bg="white",highlightbackground="white")
button.grid(row=4,column=0)

window.mainloop()

if __name__ == "__main__":
    main()