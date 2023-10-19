import time
import src.youfucktube as youfucktube

try:
    import pyperclip
except (ImportError, ImportWarning) as e:
    print(
        "Install pip packange pyperclip for this programm to work: 'pip install pyperclip'"
    )
    exit(1)

def main():
    
    prev_clipboard_content = ""
    try:
        while True: 
            # get clipboard contents
            video_url: str = pyperclip.paste()
            
            # compare to last clipboard contents
            if video_url != prev_clipboard_content:
                
                # do the thing
                try:
                    video_id = youfucktube.extract_video_id(video_url)
                    link = youfucktube.create_link(video_id)
                    youfucktube.open_browser(link)
                except ValueError:
                    pass

                # save current clipboard contents 
                prev_clipboard_content = video_url
                
            time.sleep(0.2)

    except (KeyboardInterrupt, InterruptedError, SystemExit):
        exit(0)

if __name__ == "__main__":
    main()