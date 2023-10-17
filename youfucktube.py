# /bin/python3

import subprocess

try:
    import pyperclip
except (ImportError, ImportWarning) as e:
    print(
        "Install pip packange pyperclip for this programm to work: 'pip3 install pyperclip'"
    )
    exit(1)


HTML = """<!DOCTYPE html>
<html>
<head>
<title>YouFuckTube</title>
</head>
<body>
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/{video_id}" title="YouFuckTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</body>
</html> 
"""

file_name = "fuckyoutube.html"


def main():
    video_url: str = pyperclip.paste()
    # video_url = "https://www.youtube.com/watch?v=W7tpYskJVho"
    # video_url = "https://www.youtube.com/watch?v=maqwMGuc5rs&list=PLFBHIu8sTMFKLxamcXnWmRmRhxWxmcsu6"

    if "www.youtube.com/watch" not in video_url:
        print("Please copy the Video URL into the Clipboard.")
        exit(1)

    video_id: str = video_url.split("?v=")[1]
    video_id: str = video_id.split("&")[0]

    file_content = HTML.format(video_id=video_id)

    with open(file_name, "w") as f:
        f.write(file_content)

    open_brwoser(file_name)
    exit(1)


def open_brwoser(file):
    try:
        subprocess.Popen(["firefox", file])
    except Exception:
        print(
            f'Could not open firefox. Doubleklick the "{file_name}" file to view the Video.'
        )


if __name__ == "__main__":
    main()
