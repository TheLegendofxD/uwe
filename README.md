# uwe
A very simple graphical interface for youtube-dl licensed under GLP-2.0

# Screenshots
|![Screenshot Ubuntu GTK3 with the Yaru-Theme](https://github.com/TheLegendofxD/uwe/blob/main/github_assets/uwe-yaru.png?raw=true)|![Screenshot Ubuntu Tkinter](https://github.com/TheLegendofxD/uwe/blob/main/github_assets/uwe-tk.png?raw=true)|
--- | ---
| GTK3-Version on Ubuntu | Tkinter-Version on Ubuntu |

# About
I wrote this App to faster download from YouTube.
**UWE** is short for **U**we **W**eb-Video **E**xtractor

# Installation
### Ubuntu:
  ```diff
  $ sudo apt install --upgrade python3
  ```
  
  ```diff
  $ sudo apt install --upgrade git
  ```
  
  ```diff
  $ pip install --upgrade youtube_dl
  ```
  ```diff
  $ git clone https://github.com/TheLegendofxD/uwe.git
  ```

### Windows(7+)[UWE 2.0+]:

  Go to https://python.org/downloads and download the newest version of python 3.x.
  Then go to https://git-scm.com/downloads and install Git(optinial).
  Now open the Comandpromt and type
  ```diff
  pip install --upgrade youtube_dl
  ```
  or just install the youtube_dl binaries from https://youtube-dl.org/
  
  ```diff
  git clone https://github.com/TheLegendofxD/uwe.git
  ```
  or just download the newest release from Github.

# Usage
Just run **main.py**
This can be done with:
```diff
python3 main.py
```
```diff
python main.py
```
```diff
py.exe main.py
```

or just by double clicking on the file.
Just try which of these options work for you.

If you want to use it in other python-programs:
```diff
import uwe

url = "https://www.youtube.com/watch?v=i0gZaBCR9EI"
mode = "Video" # ether "Audio" or "Video"
subs = True # Here you can say if the subtitles should be downloaded
auto_subs = False # Here you can choose if you want to download the normal subtitles or the automaticly generated subtitles
Here you can choose if the subtitles should be embedded into the video file. This could cause problems with some video players
uwe.download(url, mode, subs, auto_subs, embed_subs)
``` 
# Changelog
### 1.0
- Initial Release

### 1.1
- Added a Heading for the Subtitle-Settings
- Added Links to my Website, the Changelog and a mailto-Link to my Feedback-Email-Adress

### 2.0
- Now other Python-Programs can download Videos throw **UWE**
- Changed the Window-title to include the version number
- Removed unused Messagebox function
- Added some comments
- Added a GUI written in Tkinter and a Textmode for compability with Windows and many other operation systems
- Rewrote a lot of code because of the other changes xD
