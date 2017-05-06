'''
Tests for the Archive crawler
'''
import unittest
from app.crawler.archive import Crawler


class TestArchiveCrawling(unittest.TestCase):

    def test_ny(self):
        # Given an archive page of the NY Times
        html_data = None  # TODO get data

        # When the crawler extracts data from the archive page
        crawler = Crawler()
        page = crawler.extract(html_data)

        # Then it will have extracted the article urls
        expected_article_urls = []
        self.assertEquals(expected_article_urls, page.article_urls)
        # And it will have extracted the url to the next archive page
        expected_archive_url = ""
        self.assertEquals(expected_archive_url, page.next_page_url)

    def test_daily_times(self):
        # Given an archive page of the Daily Times
        html_data = None  # TODO get data

        # When the crawler extracts data from the archive page
        crawler = Crawler()
        page = crawler.extract(html_data)

        # Then it will have extracted the article urls
        expected_article_urls = []
        self.assertEquals(expected_article_urls, page.article_urls)
        # And it will have extracted the url to the next archive page
        expected_archive_url = ""
        self.assertEquals(expected_archive_url, page.next_page_url)
