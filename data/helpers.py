import random
import re
from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup
from requests import utils

import stored_variables


def get_response_object(url):
    """
    Returns
    - response object if success;
    - 0 if the error happens
    """

    result = None
    try:
        r = requests.get(url, allow_redirects=True)
        result = r.status_code
        if result == 200:
            return r
    except Exception as e:
        result = e
    print(f"Error {result}")
    return 0


def get_title(url):
    try:
        html = request.get(url).text
    except Exception as e:
        print(e)
        return 1
    try:
        bs = BeautifulSoup(html, "lxml")
        title = bs.body.h1
    except Exception as e:
        print(e)
        return 1
    return title


# Retrieves a list of all Internal links found on a page
def get_internal_links(bs, include_url):
    """
    Returns list
    """

    internal_links = list()
    base_url, domain = get_domain(include_url)

    # Finds all links that begin with a "/"
    try:
        links = bs.find_all("a")
    except:
        return internal_links
    for link in links:
        try:
            reference = link.attrs["href"]
            # print("INTERNAL LINK:", reference)
        except Exception as e:
            print("No, it's me!")
            print(type(e), e)
            continue
        if reference.startswith("/") or domain in reference:
            if reference.startswith("/"):
                reference = base_url + reference
            if reference not in internal_links:
                internal_links.append(reference)
    return internal_links


# Retrieves a list of all external links found on a page
def get_external_links(bs, exclude_url):
    """
    Returns: list
    """
    external_links = list()
    _, domain = get_domain(exclude_url)

    # Finds all links that start with "http" that do
    # not contain the current URL
    try:
        links = bs.find_all("a")
    except:
        return external_links
    for link in links:
        if "href" in link.attrs:
            reference = link.attrs["href"]
        else:
            continue
        if (domain not in reference) and ("http" in reference or "https" in reference):
            if reference not in external_links:
                print()
                print(domain)
                print("GO TO EXT:", reference)
                external_links.append(reference)
    return external_links


def get_random_external_link(starting_page):
    """
    Returns: string
    """
    html = requests.get(starting_page).text
    bs = BeautifulSoup(html, "lxml")
    external_links = get_external_links(bs, starting_page)
    if len(external_links) == 0:
        try:
            print("No external links, looking around the site for one")
            internal_links = get_internal_links(bs, starting_page)
            return get_random_external_link(
                internal_links[random.randint(0, len(internal_links) - 1)]
            )
        except:
            print("No external links found.")
            return 0
    else:
        return external_links[random.randint(0, len(external_links) - 1)]


def follow_external_only(starting_site):
    try:
        external_link = get_random_external_link(starting_site)
        print("Random external link: {}".format(external_link))
        follow_external_only(external_link)
    except Exception as e:
        print("Error:", e)
        return 1


def get_domain(url):
    """
    Returns: tuple
    - domain (no 'www')
    - base_url - complete url with protocol, subdomain and domain.
    """
    domain = utils.urlparse(url).netloc
    base_url = f"{utils.urlparse(url).scheme}://{domain}"
    # take only site.com
    domain_list = domain.split(".")
    domain = ".".join(domain_list[-2:])
    return base_url, domain


def get_all_ext_links(url):
    print()
    print("WORKING WITH:", url)
    r = get_response_object(url)
    if r:
        html = r.text
    else:
        return r

    bs = BeautifulSoup(html, "lxml")
    internal_links = get_internal_links(bs, url)
    external_links = get_external_links(bs, url)

    for link in external_links:
        if link not in stored_variables.all_ext_links:
            stored_variables.all_ext_links.add(link)
            print("EXTERNAL LINK:", link)
            print()
    for link in internal_links:
        if link not in stored_variables.all_int_links:
            stored_variables.all_int_links.add(link)
            get_all_ext_links(link)
