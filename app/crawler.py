'''
Crawls an XML document. It can extract urls for further crawling and optionally
store the documents it has visited.
'''
from selenium import webdriver
from queue import queue, Order
from lxml import etree


class Query():
    '''
    An instruction for how a Crawler should process a page.
    :param query: a string containing a css query, that will result in one or
                  more urls that are to extracted from the page.
    :param crawler: a string with a crawlers label.
    '''

    def __init__(self, query=None, crawler=None):
        self.query = query
        self.crawler = crawler


class Crawler():
    '''
    Crawls a page and stores its results in a datastore to await
    further processing.
    :param queries: an array of Query objects, configuring the Crawler.
    :param version: version of the Crawler implementation in case we want to
                    reprocess some urls with an updated crawler
    :param download: flag dictating if the crawler should download the file and
                     store it.
    :returns: a list of Orders
    '''

    def __init__(self, queries, version=1, download=False, wait_query=None):
        self.queries = queries
        self.version = version
        self.download = download
        self.wait_query = wait_query

        driver = webdriver.PhantomJS()
        driver.implicitly_wait(10)
        self.driver = driver

    def crawl(self, url):

        driver.get(url)
        if wait_query is not None:
            driver.find_element_by_xpath(wait_query)

        if self.download:
            self.archive(html)

        orders = self.extract(html, self.queries)
        for order in orders:
            self.queue(order)

    def extract(self, html, queries):
        tree = etree.HTML(html)
        orders = []
        for query in queries:
            urls = tree.xpath(query.query)
            for url in urls:
                orders.append(
                    Order(url, query.crawler)
                )
        return orders

    def queue(self, order):
        queue(order)

    def archive(self, html):
        raise Exception("TODO implement")
