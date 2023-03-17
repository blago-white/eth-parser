from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BinanceParser:
    def __init__(self, url: str):
        self.url = url
        self.options = webdriver.ChromeOptions()
        self.driver = self._get_driver()

    def _get_driver(self):
        self.options = self.options.add_argument(argument='headless')
        dr = webdriver.Chrome(options=self.options)
        return dr

    def get_chart_page(self):
        self.driver.get(self.url)
        return self.driver.page_source
