import requests
from bs4 import BeautifulSoup
import constant


def get_menu_page_html(page_number):
    """
    get the html of the menu pages of this course (here is an example of the menu page:
        'https://channel9.msdn.com/series/windows-10-development-for-absolute-beginners?page=2')
    :param page_number: the number after '?page=', indicates the page number of the menu of the course
    :return: an html of the menu page
    """
    r = requests.get(constant.MENU_LINK + str(page_number), headers=constant.HEADER)

    return r.text


def get_video_page_ref(page_html):
    """
    get all the link to the video page on a given menu page
    :param page_html: the html of the menu page
    :return: a list of links to all the video pages
    """
    soup = BeautifulSoup(page_html, 'lxml')

    # get all the entry meta
    metas = soup.find_all(attrs={'class': 'entry-meta'})

    # get all the title in the metas
    titles = [meta.find(attrs={'class': 'title'}) for meta in metas]

    # get the reference of the titles
    refs = ['https://channel9.msdn.com' + title['href'] for title in titles]

    return refs


def get_video_page_link(page_number):
    """
    get the video link with the given page number, this is the method used in main
    :param page_number: the number after '?page=', indicates the page number of the menu of the course
    :return: a list of links to all the video pages
    """
    html = get_menu_page_html(page_number)
    return get_video_page_ref(html)

if __name__ == '__main__':
    for item in get_video_page_link(2):
        print(item)