'''
Crawls an XML/HTML document. It can extract urls for further crawling and
optionally store the documents it has visited.
'''
import logging
from selenium import webdriver
from .queue import Order
from lxml import etree
from .processor import Archiver
import urllib.parse as urlparse


class Query(object):
    '''
    An instruction for how a Crawler should process a page.
    :param query: a string containing a css query, that will result in one or
                  more urls that are to extracted from the page.
    :param crawler: a string with a crawlers label.
    '''

    def __init__(self, query=None, crawler=None):
        self.query = query
        self.crawler = crawler


class Fetcher(object):

    def __init__(self, driver):
        self.driver = driver

    def fetch(self, url, wait_query):
        self.driver.get(url)
        if wait_query is not None:
            self.driver.find_element_by_xpath(wait_query)
        return self.driver.page_source


class PhantomFetcher(Fetcher):

    def __init__(self):
        driver = webdriver.PhantomJS()
        driver.implicitly_wait(10)
        super(PhantomFetcher, self).__init__(driver)


class Queuer(object):

    def queue(order):
        logging.warning("queing Orders isn't implemented yet")
        # TODO store the Order in the datastore


class Crawler(object):
    '''
    Crawls a page and stores its results in a datastore to await
    further processing.
    :param queries: an array of Query objects, configuring the Crawler.
    :param fetcher: an implementation of Fetcher.
    :param archiver: an implementation of Archiver.
    :param queuer: an implementation of Queuer.
    :param version: version of the Crawler implementation in case we want to
                    reprocess some urls with an updated crawler.
    :param download: flag dictating if the crawler should download the file and
                     store it.
    :param wait_query: an xpath query that must first produce at least one
                       match, before the page is used for url extraction. This
                       allows pages that use javascript to be crawled.

    :returns: a list of Orders
    '''

    def __init__(self, queries,
                 fetcher=PhantomFetcher(),
                 archiver=Archiver(),
                 queuer=Queuer(),
                 version=1,
                 download=False,
                 wait_query=None):
        self.queries = queries
        self.version = version
        self.download = download
        self.wait_query = wait_query
        self.fetcher = fetcher
        self.archiver = archiver
        self.queuer = queuer

    def crawl(self, url):
        html = self.fetcher.fetch(url, self.wait_query)
        if self.download:
            self.archiver.archive(html)

        orders = self.extract(url, html, self.queries)
        for order in orders:
            self.queuer.que(order)

    def extract(self, original_url, html, queries):
        tree = etree.HTML(html)
        orders = []
        for query in queries:
            urls = tree.xpath(query.query)
            for url in urls:
                orders.append(
                    Order(urlparse.urljoin(original_url, url), query.crawler)
                )
        return orders
