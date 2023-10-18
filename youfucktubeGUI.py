# /bin/python3

import tkinter as tk
import webbrowser

app = tk.Tk()
app.title("YouFuckTubeGUI")
app.geometry("400x150")
app.configure(bg="#252526")

normal_font = ("Helvetica", 10)
bold_font = ("Helvetica", 12, "bold")

spacer_label = tk.Label(app, text="", bg="#252526").pack()

input_label = tk.Label(app, text="Youtube URL:", font=bold_font, fg="white", bg="#252526")
input_label.pack()

url = tk.Entry(app, width=50, font=normal_font)
url.pack()

embed_link = "https://www.youtube-nocookie.com/embed/{video_id}"

file_name = "fuckyoutube.html"

err_msg = tk.StringVar()


def check_link():
    video_url: str = url.get()
    err_msg.set("")

    if "www.youtube.com/watch?v=" not in video_url:
        err_msg.set("Please copy the Video URL into the Clipboard.")
        return

    video_id: str = video_url.split("?v=")[1]
    video_id: str = video_id.split("&")[0]

    link = embed_link.format(video_id=video_id)
    open_browser(link)


def open_browser(url: str):
    try:
        # tries to open a new tab instead of a new window
        webbrowser.get().open(url=url, new=2)
    except Exception:
        err_msg.set(f"Could not open default browser. Here is your link: {url}")


spacer_label2 = tk.Label(app, text="", bg="#252526").pack()

submit_button = tk.Button(app, text="Submit", command=check_link, font=bold_font, bg="#007acc", fg="white", borderwidth=1)
submit_button.pack()

warning_label = tk.Label(app, textvariable=err_msg, fg="#dadf49", bg="#252526", font=normal_font)
warning_label.pack()

app.mainloop()