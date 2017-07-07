from selenium import webdriver
import requests

class Fetcher(object):

    def fetch(self, url, wait_query):
        raise Exception("Fetcher.fetch() must be extended")


class RequestFetcher(Fetcher):

    def fetch(self, url, wait_query):
        response = requests.get(url)
        if wait_query is not None:
            raise Exception("wait_query is not supported by RequestFetcher")
        return response.content


class PhantomFetcher(Fetcher):

    def __init__(self):
        self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(10)

    def fetch(self, url, wait_query):
        self.driver.get(url)
        if wait_query is not None:
            self.driver.find_element_by_xpath(wait_query)
        return self.driver.page_source
