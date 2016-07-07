import constant
import requests
import config
from bs4 import BeautifulSoup


def get_video_page_html(video_page_link):
    """
    get the html of the video page, here is an example of the video page:
        https://channel9.msdn.com/Series/Windows-10-development-for-absolute-beginners/UWP-031-Stupendous-Styles-Challenge
    :param video_page_link: the link of the video page(like the link above)
    :return: the html of the given video page
    """
    r = requests.get(video_page_link, headers=constant.HEADER)

    return r.text


def get_video_ref(html):
    soup = BeautifulSoup(html, 'lxml')

    # get all the download link div (i don't know why it have class help)
    divs = soup.find_all(attrs={'class': 'help'})

    # div[0] is a useless help file
    # div[1] is the MP3 Version
    # div[2] is the Low Quality version
    # div[3] is the High Quality version
    # div[4] is the Mid Quality version
    # you can change this configuration in config.py.
    try:
        video_quality_index = constant.VIDEO_QUALITY_INDEX_MAP[config.video_quality]
    except KeyError:
        raise ValueError('the video quality you input in the config file is invalid.')
    high_quality_video_div = divs[video_quality_index]

    # get the video link, find the <a> tag, and extract the 'href'
    video_ref = high_quality_video_div.find('a')['href']

    return video_ref


def get_video_link(video_page_link):
    html = get_video_page_html(video_page_link)
    return get_video_ref(html)

if __name__ == '__main__':
    get_video_link('https://channel9.msdn.com/Series/Windows-10-development-for-absolute-beginners/UWP-031-Stupendous-Styles-Challenge')