'''
Tests for the Archive crawler
'''
import unittest
import os
from crawler.crawler import Crawler

test_dir_path = os.path.dirname(__file__)


class MockFetcher():
    def __init__(self, page_source):
        self.page_source = page_source

    def fetch(self, url, wait_query):
        return self.page_source


class TestArchiveCrawling(unittest.TestCase):

    def setUp(self):
        # Given an archive page of the NY Times
        test_data_path = os.path.join(test_dir_path, 'data/ny_archive_sample.html')
        with open(test_data_path, 'r', encoding='cp1251') as f:
            self.html_data = f.read().replace('\n', '')
        # And a Crawler configured to extract article urls
        self.queries = [
            "//li[@class='story noThumb']//a/@href",
        ]

    def test_extraction(self):
        crawler = Crawler(
            self.queries,
            fetcher=MockFetcher(self.html_data)
        )

        # When the crawler extracts data from the archive page
        test_url = "https://query.nytimes.com/search/sitesearch/#/*/from19810101to20171231/document_type%3A%22article%22/1/allauthors/oldest/"
        result = crawler.crawl(test_url)

        # Then it will have queued the Orders
        expected = [
            "https://www.nytimes.com/1981/01/01/nyregion/notes-on-people-207391.html",
            "https://www.nytimes.com/1981/01/01/obituaries/marshall-mcluhan-author-dies-declared-medium-is-the-message.html",
            "https://www.nytimes.com/1981/01/01/business/thursday-january-1-1981-the-economy.html",
            "https://www.nytimes.com/1981/01/01/arts/wncn-fm-is-put-up-for-sale-by-gaf.html",
            "https://www.nytimes.com/1981/01/01/nyregion/new-year-s-day.html",
            "https://www.nytimes.com/1981/01/01/us/around-the-nation-irs-seeking-16.6-million-in-back-taxes-from-welch.html",
            "https://www.nytimes.com/1981/01/01/us/no-headline-207370.html",
            "https://www.nytimes.com/1981/01/01/nyregion/7koch-box-a-caution-from-koch-on-investing-in-camels.html",
            "https://www.nytimes.com/1981/01/01/world/chomsky-stirs-french-storm-in-a-demitasse.html",
            "https://www.nytimes.com/1981/01/01/nyregion/45-year-terms-given-2-in-bank-robberies.html",
        ]
        self.assertEquals(len(expected), len(result))
        for index, expexted_url in enumerate(expected):
            result_url = result[index]
            self.assertEquals(expexted_url, result_url)
