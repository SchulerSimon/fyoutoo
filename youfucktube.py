# /bin/python3

import time
import subprocess

try:
    import pyperclip
except (ImportError, ImportWarning) as e:
    print(
        "Install pip packange pyperclip for this programm to work: 'pip3 install pyperclip'"
    )
    exit(1)


video_embedded_url = (
    '<iframe width="560" height="315" '
    + 'src="www.youtube-nocookie.com/embed/{video_id}" '
    + 'title="YouTube video player" frameborder="0" '
    + 'allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; '
    + 'picture-in-picture; web-share" allowfullscreen></iframe>'
)

temp_file_name = "fuckyoutube.html"


def main():
    video_url: str = pyperclip.paste()
    # video_url = "https://www.youtube.com/watch?v=W7tpYskJVho"
    # video_url = "https://www.youtube.com/watch?v=maqwMGuc5rs&list=PLFBHIu8sTMFKLxamcXnWmRmRhxWxmcsu6"

    if "www.youtube.com/watch" not in video_url:
        print("Please copy the Video URL into the Clipboard.")
        exit(1)

    video_id: str = video_url.split("?v=")[1]
    video_id: str = video_id.split("&")[0]

    file_content = ""

    try:
        with open(temp_file_name, "r") as f:
            file_content = f.read()
    except FileNotFoundError:
        pass

    file_content = video_embedded_url.format(video_id=video_id) + "\n" + file_content

    with open(temp_file_name, "w") as f:
        f.write(file_content)

    subprocess.Popen(["firefox", temp_file_name])
    time.sleep(1)
    exit(1)


if __name__ == "__main__":
    main()
