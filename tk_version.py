from tkinter import *
import uwe, webbrowser

VERSION = 2.0
WIN_TITLE = f"Uwe v{VERSION} (Tkinter)"
PRODUCT = "Uwe_TK"

def dwnld_vid(url, subs, autosubs, embedsubs):
	uwe.download(url, "Video", subs.get(), autosubs.get(), embedsubs.get())

def dwnld_aud(url):
	uwe.download(url, "Audio")

def open_link(url):
	webbrowser.open(url)


root = Tk()

root.title(WIN_TITLE)

Label(root, text="YouTube-Url: ").grid(row=0)
youtube_url = Entry(root)
youtube_url.grid(row=0, column=1)
Label(root, text="Subtitles Settings(Video Only):").grid(row=1, column=0)
dwnld_subs = IntVar()
Checkbutton(root, text="Download Subtitles: ", variable=dwnld_subs).grid(row=2, column=0)
auto_subs = IntVar()
Checkbutton(root, text="Use Auto-Subs: ", variable=auto_subs).grid(row=3, column=0)
embed_subs = IntVar()
Checkbutton(root, text="Embed Subs: ", variable=embed_subs).grid(row=4, column=0)
download_video_btn = Button(root, text="Download Video", command=lambda: dwnld_vid(youtube_url.get(), dwnld_subs, auto_subs, embed_subs)).grid(row=5, column=0)
download_audio_btn = Button(root, text="Download Audio", command=lambda: dwnld_aud(youtube_url.get())).grid(row=5, column=1)

link1 = Label(root, text="Changelog", fg="blue", cursor="hand2")
link1.grid(row=6, column=0)
link2 = Label(root, text="Feedback", fg="blue", cursor="hand2")
link2.grid(row=6, column=1)
link1.bind("<Button-1>", lambda e: open_link("https://github.com/TheLegendofxD/uwe#Changelog"))
link2.bind("<Button-1>", lambda e: open_link(f"mailto:legendxd@magenta.de?subject={PRODUCT}_v{str(VERSION)}_Feedback"))

root.mainloop()
