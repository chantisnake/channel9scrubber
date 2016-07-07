import wget


def download_video(video_link):
    filename = wget.download(video_link)
