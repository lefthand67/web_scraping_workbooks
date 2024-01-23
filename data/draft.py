from urllib.request import urlopen

from bs4 import BeautifulSoup


def main():
    html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
    bs = BeautifulSoup(html, "html.parser")

    title = bs.find_all(id="text", class_="red")
    for t in title:
        print(t.get_text())


main()
