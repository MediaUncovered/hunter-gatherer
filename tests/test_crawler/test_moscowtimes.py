'''
Tests for the Moscow times crawlers
'''
import unittest
import os
from app.crawler import Crawler, Query
from app.queue import Order

test_dir_path = os.path.dirname(__file__)


class MockFetcher():
    def __init__(self, page_source):
        self.page_source = page_source

    def fetch(self, url, wait_query):
        return self.page_source


class MockQueuer():

    def __init__(self):
        self.orders = []

    def que(self, order):
        self.orders.append(order)


class TestYearCrawling(unittest.TestCase):

    def setUp(self):
        # Given an archive page of the NY Times
        test_data_path = os.path.join(test_dir_path, 'data/themoscowtimes_years_sample.html')
        with open(test_data_path, 'r') as f:
            self.html_data = f.read().replace('\n', '')
        # And a Crawler configured to extract article urls
        self.queries = [
            Query(
                query="//div[@class='block_left']//a/@href",
                crawler="MOSCOW_MONTH"
            )
        ]

    def test_extraction(self):
        crawler = Crawler(
            self.queries,
            fetcher=MockFetcher(self.html_data),
            queuer=MockQueuer()
        )

        # When the crawler extracts data from the archive page
        test_url = "https://old.themoscowtimes.com/sitemap/"
        crawler.crawl(test_url)

        # Then it will have queued the Orders
        expected = [
            Order("https://old.themoscowtimes.com/sitemap/free/2017.html", "MOSCOW_MONTH"),
            Order("https://old.themoscowtimes.com/sitemap/free/2016.html", "MOSCOW_MONTH"),
            Order("https://old.themoscowtimes.com/sitemap/free/2015.html", "MOSCOW_MONTH"),
            Order("https://old.themoscowtimes.com/sitemap/free/2014.html", "MOSCOW_MONTH"),
            Order("https://old.themoscowtimes.com/sitemap/free/2013.html", "MOSCOW_MONTH"),
            Order("https://old.themoscowtimes.com/sitemap/free/2012.html", "MOSCOW_MONTH"),
            Order("https://old.themoscowtimes.com/sitemap/free/2011.html", "MOSCOW_MONTH"),
            Order("https://old.themoscowtimes.com/sitemap/free/2010.html", "MOSCOW_MONTH"),
            Order("https://old.themoscowtimes.com/sitemap/free/2009.html", "MOSCOW_MONTH"),
            Order("https://old.themoscowtimes.com/sitemap/free/2008.html", "MOSCOW_MONTH"),
            Order("https://old.themoscowtimes.com/sitemap/free/2007.html", "MOSCOW_MONTH"),
            Order("https://old.themoscowtimes.com/sitemap/free/2006.html", "MOSCOW_MONTH"),
            Order("https://old.themoscowtimes.com/sitemap/free/2005.html", "MOSCOW_MONTH"),
            Order("https://old.themoscowtimes.com/sitemap/free/2004.html", "MOSCOW_MONTH"),
            Order("https://old.themoscowtimes.com/sitemap/free/2003.html", "MOSCOW_MONTH"),
            Order("https://old.themoscowtimes.com/sitemap/free/2002.html", "MOSCOW_MONTH"),
            Order("https://old.themoscowtimes.com/sitemap/free/2001.html", "MOSCOW_MONTH"),
            Order("https://old.themoscowtimes.com/sitemap/free/2000.html", "MOSCOW_MONTH"),
            Order("https://old.themoscowtimes.com/sitemap/free/1999.html", "MOSCOW_MONTH"),
            Order("https://old.themoscowtimes.com/sitemap/free/1998.html", "MOSCOW_MONTH"),
            Order("https://old.themoscowtimes.com/sitemap/free/1997.html", "MOSCOW_MONTH"),
            Order("https://old.themoscowtimes.com/sitemap/free/1996.html", "MOSCOW_MONTH"),
            Order("https://old.themoscowtimes.com/sitemap/free/1995.html", "MOSCOW_MONTH"),
            Order("https://old.themoscowtimes.com/sitemap/free/1994.html", "MOSCOW_MONTH"),
            Order("https://old.themoscowtimes.com/sitemap/free/1993.html", "MOSCOW_MONTH"),
            Order("https://old.themoscowtimes.com/sitemap/free/1992.html", "MOSCOW_MONTH")
        ]
        self.assertEquals(len(expected), len(crawler.queuer.orders))
        for index, expected_order in enumerate(expected):
            result_order = crawler.queuer.orders[index]
            self.assertEquals(expected_order.url, result_order.url)
            self.assertEquals(expected_order.crawler_label, result_order.crawler_label)
