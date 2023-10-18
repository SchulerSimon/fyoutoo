# /bin/python3

import webbrowser

embed_link = "https://www.youtube-nocookie.com/embed/{video_id}"


def extract_video_id(video_url: str) -> str:
    """takes a youtube url and extracts the video_id

    Args:
        video_url (str): url to a youtube video

    Raises:
        ValueError: when the given video_url is not a valid youtube.com/watch link

    Returns:
        str: the unique video_id
    """
    if "www.youtube.com/watch" not in video_url:
        raise ValueError("Must provide a youtube.com/watch?v=<video_id> link")

    video_id: str = video_url.split("?v=")[1]
    video_id: str = video_id.split("&")[0]
    return video_id


def create_link(video_id: str) -> str:
    """creates the embedded link

    Args:
        video_id (str): the url of the video

    Returns:
        str: a link to an embedded version of the video
    """
    link = embed_link.format(video_id=video_id)
    return link


def open_browser(url: str):
    """opens the system default browser with the given url

    Args:
        url (str): the url to be displayed in a new tab
    """
    try:
        # tries to open a new tab instead of a new window
        webbrowser.get().open(url=url, new=2)
    except Exception:
        print(f"Could not open default browser. Here is your link: {url}")
        exit(1)
