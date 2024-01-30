import random
import re
import signal
import sys
from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup
from requests import utils

import helpers
import stored_variables


def main():
    # catching keyboardInterrtupt
    signal.signal(signal.SIGINT, helpers.signal_handler)

    url = "http://oreilly.com"
    stored_variables.all_int_links.add(url)
    helpers.get_all_ext_links(url)


if __name__ == "__main__":
    main()
