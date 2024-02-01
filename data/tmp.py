class Webpage:
    """Common base class for all articles/pages"""

    def __init__(self, name, url, title_tag):
        self.name = name
        self.url = url
        self.title_tag = title_tag


class Product(Webpage):
    """Contains information for scraping a product page"""

    def __init__(self, name, url, title_tag, product_number_tag, price_tag):
        super().__init__(name, url, title_tag)
        self.product_number_tag = product_number_tag
        self.price_tag = price_tag


class Article(Webpage):
    """Contains information for scraping an article page"""

    def __init__(self, name, url, title_tag, body_tag, date_tag):
        super().__init__(name, url, title_tag)
        self.body_tag = body_tag
        self.date_tag = date_tag
