'''
Tests for the Archive crawler
'''
import unittest
import os
from app.crawler import Crawler, Query
from app.queue import Order

test_dir_path = os.path.dirname(__file__)


class MockDriver():
    def __init__(self, page_source):
        self.page_source = page_source


class TestArchiveCrawling(unittest.TestCase):

    def setUp(self):
        # Given an archive page of the NY Times
        test_data_path = os.path.join(test_dir_path, 'ny_archive_sample.html')
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
            self.queries
        )

        # When the crawler extracts data from the archive page
        result = crawler.extract(self.html_data, crawler.queries)

        # Then it will have extracted the Orders
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
        self.assertEquals(len(expected), len(result))
        for index, expected_order in enumerate(expected):
            result_order = result[index]
            self.assertEquals(expected_order.url, result_order.url)
            self.assertEquals(expected_order.crawler, result_order.crawler)
