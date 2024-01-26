import datetime
import random
import re
from urllib.request import urlopen

from bs4 import BeautifulSoup

LIMIT = 20


def main():
    links = get_links("/wiki/Joseph_Stalin")

    count = 0
    while len(links) > 0:
        new_article = links[random.randint(0, len(links) - 1)].attrs["href"]
        print(new_article)
        links = get_links(new_article)
        count += 1
        if count == LIMIT:
            break
    return 0


def get_links(url):
    html = urlopen(f"https://en.wikipedia.org{url}")
    bs = BeautifulSoup(html, "lxml")

    return bs.find("div", {"id": "bodyContent"}).find_all(
        "a", href=re.compile("^(/wiki/)((?!:).)*$")
    )


if __name__ == "__main__":
    main()
