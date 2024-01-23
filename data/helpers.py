from urllib.request import urlopen

from bs4 import BeautifulSoup


def get_title(url):
    try:
        html = urlopen(url)
    except Exception as e:
        print(e)
        return None
    try:
        bs = BeautifulSoup(html, "html.parser")
        title = bs.body.h1
    except Exception as e:
        print(e)
        return None
    return title
