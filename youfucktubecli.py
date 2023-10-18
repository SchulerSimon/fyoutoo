import youfucktube

try:
    import pyperclip
except (ImportError, ImportWarning) as e:
    print(
        "Install pip packange pyperclip for this programm to work: 'pip install pyperclip'"
    )
    exit(1)

def main():
    video_url: str = pyperclip.paste()

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
