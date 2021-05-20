#!/usr/bin/env python3
import os

# Module-Functions
def download(url: str,type: str = "Video", subtitles: bool = False, embed_subs: bool = False, auto_subs: bool = False):
	if type == "Video":
		cmd = "youtube-dl"
	elif type == "Audio":
		cmd = "youtube-dl -x"
	
	if subtitles and type == "Video":
		if auto_subs:
			cmd += " --write-auto-sub"
		else:
			cmd += " --write-srt"
		
		if embed_subs:
			cmd += " --embed-subs"
	
	cmd += f" {url}"
	
	os.system(cmd)