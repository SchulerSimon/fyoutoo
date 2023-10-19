import tkinter as tk
import src.youfucktube as youfucktube


def main():
    app = tk.Tk()
    app.title("YouFuckTubeGUI")
    app.geometry("400x150")
    app.configure(bg="#252526")

    normal_font = ("Helvetica", 10)
    bold_font = ("Helvetica", 12, "bold")

    spacer_label = tk.Label(app, text="", bg="#252526").pack()

    input_label = tk.Label(
        app, text="Youtube URL:", font=bold_font, fg="white", bg="#252526"
    )
    input_label.pack()

    url = tk.Entry(app, width=50, font=normal_font)
    url.pack()

    err_msg = tk.StringVar()

    spacer_label2 = tk.Label(app, text="", bg="#252526").pack()

    def button_press():
        video_url: str = url.get()

        err_msg.set("")

        try:
            video_id: str = youfucktube.extract_video_id(video_url)
        except ValueError:
            err_msg.set("Please input a valid youtube URL.")
            return

        link = youfucktube.create_link(video_id)
        youfucktube.open_browser(link)

        return

    submit_button = tk.Button(
        app,
        text="Submit",
        command=button_press,
        font=bold_font,
        bg="#007acc",
        fg="white",
        borderwidth=1,
    )
    submit_button.pack()

    warning_label = tk.Label(
        app, textvariable=err_msg, fg="#dadf49", bg="#252526", font=normal_font
    )
    warning_label.pack()

    app.mainloop()


if __name__ == "__main__":
    main()
