# YouFuckTube - UNBLOCK YOUTUBE ADBLOCK-BLOCK

## Tired of this?
![YouFuckTube-Adblock-blcoker](adblock-blocker.png)

# Here is your solution! 

## What do you need to do?

- install [Pyhton3](https://www.python.org/downloads/): 
    - Linux: `sudo apt install python3.12` 
    - Windows: click [here](https://www.python.org/downloads/)
    - MacOS: click [here](https://www.python.org/downloads/)
- install [pyperclip](https://pypi.org/project/pyperclip/):
    - `pip install pyperclip`
- clone this repo: 
    - `git clone https://github.com/SchulerSimon/youfucktube.git`
- copy the URL of a youtube-video
    - `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
- execute the script: 
    - `cd youfucktube`
    - CLI: 
      - Dose it once, needs to be executed each time you copy a youtube-url.
      - `python youfucktube.py`
    - GUI: 
      - Provides a Graphical User Interface you can interact with. 
      - `python youfucktubegui.py`
    - SERVICE:
      - Runs in the background. Just start the script once. And every time you copy a youtube-url, it should open a new window in the browser. 
      - `python youfucktubeforever.py`

## How dose it work?
Its super simple: *YouTube's AdBlock-Block only works on their website. When you embed a Video into another website, you can watch it just fine. This script basically automates that process.* 

- **copies** a youtube-link from your **clipboard**
- extracts the `video_id` from the link 
- creates a new link (like so `https://www.youtube-nocookie.com/embed/<video_id>`)
- calls the system-default browser to open this link and brings the browser to the front

## Things that could be improved:
- test MacOS, I cannot, have no mac. 
- build into standalone executable
- try multiple browsers, when `webbrowser.get().open(link)` fails


## How to write extension for youfucktube?
- Have a look at this [example](extension_example_youfucktube.py). 

PRs are welcome!


### Contributions: 
- Thanks to [MadaHaz](https://github.com/MadaHaz) there is also a Version with a GUI. 
- Thanks to the Idea of [granlem](https://github.com/granlem), there is also a Version that runs in the background like a service. 