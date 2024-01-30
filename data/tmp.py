import requests
from bs4 import BeautifulSoup


class Crawler:
    def get_page(self, url):
        try:
            req = resuests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, "lxml")

    def safe_get(self, page_obj, selector):
        child_obj = page_obj.select(selector)
        if child_obj is not None and len(child_obj) > 0:
            return child_obj[0].get_text()
        return ""

    def search(self, topic, site):
        """
        Searches a given website for a given topic and records all pages found
        """
        bs = self.get_page(site.search_url + topic)
        search_results = bs.select(site.result_listing)
        for result in search_results:
            url = result.select()
