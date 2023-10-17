# YouFuckTube - UNBLOCK YOUTUBE ADBLOCK-BLOCK

## Tired of this?
![YouFuckTube-Adblock-blcoker](adblock-blocker.png)

## Here is your solution: 

## What do I need to do?

- use **Linux**! 
    - Maybe one of you wants to add Windows support?!
- install [Pyhton3](https://www.python.org/downloads/): 
    - `sudo apt install python3.12` 
- install [pyperclip](https://pypi.org/project/pyperclip/):
    - `pip install pyperclip`
- clone this repo: 
    - `git clone https://github.com/SchulerSimon/youfucktube.git`
- copy the URL of a youtube-video
    - `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
- execute the script: 
    - `cd youfucktube`
    - `python3 youfucktube.py`

## How dose it work?
Its super simple: 
- **copies** a youtube-link from your **clipboard**
- creates a new HTML-file (fuckyoutube.html)
- embeds the youtube video into that file
- calls firefox to **open** that HTML-file

## Things that could be better with this:
- Windows support
- Default-Browser support
- dicrectly tell the browser to open the link: https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ
