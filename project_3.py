from __future__ import unicode_literals
from tkinter import *
import youtube_dl
import urllib
import shutil

flag=1
web_url=''

def show_entry_fields():
	web_url=e1.get()
	print(web_url)
	compile_message='Downloading'
	ydl_opts = {}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([web_url])

master = Tk()

master.title='Youtube Downloader'

Label(master, text="Enter Youtube URL").grid(row=0)

e1 = Entry(master)

e1.grid(row=0, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Begin Download', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

compile_message='Ready for download'
Label(master, text= compile_message,fg='dark green',anchor='center', textvariable=compile_message).grid(row=4)

mainloop( )

