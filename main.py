from tkinter import *
from tkinter import filedialog
from pytube import YouTube
import os


def file_selector():
    global path
    path = filedialog.askdirectory()


def yt_download():
    link = e1.get()
    global path

    if not path:
        path = os.getcwd()

    try:
        yt = YouTube(link)
        yt.streams.get_highest_resolution().download(output_path=path)
    except:
        pass


root = Tk()
root.geometry('500x500')
root.title('YT Downloader')

path = ''

l1 = Label(text='YouTube link:')
l1.pack()

e1 = Entry(bd=2)
e1.pack()

l2 = Label(text='Choose output file:')
l2.pack()

btn1 = Button(text='Choose file', command=file_selector)
btn1.pack()

btn2 = Button(text='Confirm', command=yt_download)
btn2.pack()

root.mainloop()
