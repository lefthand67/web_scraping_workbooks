import random
import re
from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup
from requests import utils

import helpers
import stored_variables


def main():
    url = "http://oreilly.com"
    stored_variables.all_int_links.add(url)
    helpers.get_all_ext_links(url)

    print("---")
    print(stored_variables.all_ext_links)
    print("---")
    print(stored_variables.all_int_links)


if __name__ == "__main__":
    main()
