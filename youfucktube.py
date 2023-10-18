# /bin/python3

import webbrowser

try:
    import pyperclip
except (ImportError, ImportWarning) as e:
    print(
        "Install pip packange pyperclip for this programm to work: 'pip install pyperclip'"
    )
    exit(1)

embed_link = "https://www.youtube-nocookie.com/embed/{video_id}"

file_name = "fuckyoutube.html"


def main():
    video_url: str = pyperclip.paste()

    if "www.youtube.com/watch" not in video_url:
        print("Please copy the Video URL into the Clipboard.")
        exit(1)

    video_id: str = video_url.split("?v=")[1]
    video_id: str = video_id.split("&")[0]

    link = embed_link.format(video_id=video_id)

    open_browser(link)
    exit(0)


def open_browser(url: str):
    try:
        # tries to open a new tab instead of a new window
        webbrowser.get().open(url=url, new=2)
    except Exception:
        print(f"Could not open default browser. Here is your link: {url}")
        exit(1)


if __name__ == "__main__":
    main()
