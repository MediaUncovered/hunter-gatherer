'''
Tests for analyzing and labeling a Moscow Times article
'''
import unittest
import os
import datetime
from app.config import Query
from app.processor import Processor

test_dir_path = os.path.dirname(__file__)


class TestProcessingMoscowTimes(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None

        title_queries = [
            Query(
                query="//div[@class='article_wrap']//h2/text()"
            )
        ]
        body_queries = [
            Query(
                query="//div[@class='article_text']//p/text()"
            )
        ]
        subject = Processor(title_queries=title_queries,
                            body_queries=body_queries)

        # Given an article page of the Moscow Times
        source_url = "http://old.themoscowtimes.com/sitemap/free/2014/1/article/netherlands-extradites-russian-accused-of-overseeing-shipments-of-cocaine-stashed-in-bananas/492579.html"
        test_data_path = os.path.join(test_dir_path, 'data/moscowtimes_sample.html')
        with open(test_data_path, 'rb') as f:
            html_data = f.read()

        # When the article is processed by the Processor class
        self.result = subject.process(source_url, html_data, 'latin-1')

    def test_title(self):
        # Then it extracts its title
        expected_title = "Netherlands Extradites Russian Accused of Overseeing Shipments of Cocaine Stashed in Bananas"
        self.assertEquals(expected_title, self.result.title)

    def test_date(self):
        # Then it extracts the publication date
        expected_datetime = datetime.datetime(2014, 1, 14)
        self.assertEquals(expected_datetime, self.result.datetime)

    def test_body(self):
        # Then it extracts content
        body_data_path = os.path.join(test_dir_path, 'data/moscowtimes_body.txt')
        with open(body_data_path, 'r', encoding='utf-8') as f:
            body = f.read()
        self.assertEquals(body, self.result.body)
