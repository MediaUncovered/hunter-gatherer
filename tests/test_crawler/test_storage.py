'''
Tests if the crawler stores data
'''
import unittest
import unittest.mock as mock
import os
from app.crawler import Crawler
from app.storage import Archiver

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


class TestCrawlerStorage(unittest.TestCase):

    def setUp(self):
        # Given an archive page of the NY Times
        test_data_path = os.path.join(test_dir_path, 'data/ny_archive_sample.html')
        with open(test_data_path, 'r', encoding='cp1251') as f:
            self.html_data = f.read().replace('\n', '')
        # And a Crawler configured to download its target
        # But not to collect any link
        self.archiver = unittest.mock.create_autospec(Archiver)
        queries = []
        self.crawler = Crawler(
            queries,
            fetcher=MockFetcher(self.html_data),
            queuer=MockQueuer(),
            archiver=self.archiver,
            download=True
        )

    def test_storage(self):
        # When the crawler crawls the page
        test_url = "https://query.nytimes.com/search/sitesearch/#/*/from19810101to20171231/document_type%3A%22article%22/1/allauthors/oldest/"
        self.crawler.crawl(test_url)

        # Then it will call the Archiver to store the data
        self.archiver.archive.assert_called_once_with(test_url, self.html_data)
        # And not queue any other jobs
        self.assertEquals(0, len(self.crawler.queuer.orders))
