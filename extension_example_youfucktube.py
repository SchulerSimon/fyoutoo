# This file gives an example on how to extend youfucktube
# it just uses a given video_url as example

from . import youfucktube


def main():
    video_url: str = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

    try:
        video_id = youfucktube.extract_video_id(video_url)
    except ValueError:
        print("Please copy the Video URL into the Clipboard.")
        exit(1)

    link = youfucktube.create_link(video_id)
    youfucktube.open_browser(link)
    exit(0)


if __name__ == "__main__":
    main()
