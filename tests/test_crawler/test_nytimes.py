'''
Tests for the Archive crawler
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


class TestArchiveCrawling(unittest.TestCase):

    def setUp(self):
        # Given an archive page of the NY Times
        test_data_path = os.path.join(test_dir_path, 'data/ny_archive_sample.html')
        with open(test_data_path, 'r') as f:
            self.html_data = f.read().replace('\n', '')
        # And a Crawler configured to extract article urls
        self.queries = [
            Query(
                query="//li[@class='story noThumb']//a/@href",
                crawler="ARTICLE"
            )
        ]

    def test_extraction(self):
        crawler = Crawler(
            self.queries,
            fetcher=MockFetcher(self.html_data),
            queuer=MockQueuer()
        )

        # When the crawler extracts data from the archive page
        test_url = "https://query.nytimes.com/search/sitesearch/#/*/from19810101to20171231/document_type%3A%22article%22/1/allauthors/oldest/"
        crawler.crawl(test_url)

        # Then it will have queued the Orders
        expected = [
            Order("https://www.nytimes.com/1981/01/01/nyregion/notes-on-people-207391.html", "ARTICLE"),
            Order("https://www.nytimes.com/1981/01/01/obituaries/marshall-mcluhan-author-dies-declared-medium-is-the-message.html", "ARTICLE"),
            Order("https://www.nytimes.com/1981/01/01/business/thursday-january-1-1981-the-economy.html", "ARTICLE"),
            Order("https://www.nytimes.com/1981/01/01/arts/wncn-fm-is-put-up-for-sale-by-gaf.html", "ARTICLE"),
            Order("https://www.nytimes.com/1981/01/01/nyregion/new-year-s-day.html", "ARTICLE"),
            Order("https://www.nytimes.com/1981/01/01/us/around-the-nation-irs-seeking-16.6-million-in-back-taxes-from-welch.html", "ARTICLE"),
            Order("https://www.nytimes.com/1981/01/01/us/no-headline-207370.html", "ARTICLE"),
            Order("https://www.nytimes.com/1981/01/01/nyregion/7koch-box-a-caution-from-koch-on-investing-in-camels.html", "ARTICLE"),
            Order("https://www.nytimes.com/1981/01/01/world/chomsky-stirs-french-storm-in-a-demitasse.html", "ARTICLE"),
            Order("https://www.nytimes.com/1981/01/01/nyregion/45-year-terms-given-2-in-bank-robberies.html", "ARTICLE")
        ]
        self.assertEquals(len(expected), len(crawler.queuer.orders))
        for index, expected_order in enumerate(expected):
            result_order = crawler.queuer.orders[index]
            self.assertEquals(expected_order.url, result_order.url)
            self.assertEquals(expected_order.crawler_label, result_order.crawler_label)
