#!/usr/bin/env python3

def gtk_version():
	import gtk_version

def tkinter_version():
	import tk_version

# Launch App
if __name__ == "__main__":
	try:
		import gi
		gui_toolkit = "gtk"
	except ImportError:
		from Tkinter import *
		gui_toolkit = "tk"
	
	if gui_toolkit == "gtk":
		gtk_version()
	elif gui_toolkit == "tk":
		tkinter_version()
	else:
		print("ERROR: No supported GUI-Toolkit installed. Instead of a GUI you'll get a textbased UI")
		import uwe
		print("######### UWE 2.0 - Text #########")
		url = input("Please enter the URL:\n")
		mode = input("Do you want to download it as Audio or as Video? (a/v)\n")
		if mode == "v":
			subs = input("Do you want to download the subtitles? (y/n)\n")
			if subs == "y":
				subs = True
				auto_subs = input("Do you want to use Auto-Subtitles? (y/n)\n")
				if auto_subs == "y":
					auto_subs = True
				else:
					auto_subs = False
				embed_subs = input("Do you want to embed the subtitles into the video-file? (y/n)\n")
				if embed_subs == "y":
					embed_subs = True
				else:
					embed_subs = False
			else:
				subs = False
				auto_subs = False
				embed_subs = False
			uwe.download(url, "Video", subs, auto_subs, embed_subs)
		elif mode == "a":
			uwe.download(url, "Audio")
		else:
			print(f"'{mode}' is not a valid option. Please ether type 'a' for Audio or 'v' for Video.")
