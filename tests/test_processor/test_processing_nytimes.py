'''
Tests for analyzing and labeling a Moscow Times article
'''
import unittest
import os
import datetime
from dateutil.tz import tzoffset
from crawler.config import Query
from crawler.processor import Processor

test_dir_path = os.path.dirname(__file__)


class TestProcessingNyTimes(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None

        title_queries = [
            Query(
                query="//article//h1/text()"
            )
        ]
        body_queries = [
            Query(
                query="//article//p[@class='story-body-text story-content']//text()"
            )
        ]
        date_queries = [
            Query(
                query="//time[@class='dateline']/@datetime"
            )
        ]
        date_format=None
        subject = Processor(title_queries=title_queries,
                            body_queries=body_queries,
                            date_queries=date_queries,
                            date_format=date_format)

        # Given an article page of the NY Times
        source_url = "https://www.nytimes.com/reuters/2017/05/22/us/politics/22reuters-usa-budget.html"
        test_data_path = os.path.join(test_dir_path, 'data/nytimes_sample.html')
        with open(test_data_path, 'rb') as f:
            html_data = f.read()

        # When the article is processed by the Processor class
        self.result = subject.process(source_url, html_data)

    def test_title(self):
        # Then it extracts its title
        expected_title = "Trump Budget Poised to Slash Healthcare for Poor, Other Programs"
        self.assertEquals(expected_title, self.result.title)

    def test_date(self):
        # Then it extracts the publication date
        expected_datetime = datetime.datetime(2017, 5, 22, 13, 15, 31, tzinfo=tzoffset(None, -14400))
        self.assertEquals(expected_datetime, self.result.date)

    def test_body(self):
        # Then it extracts content
        body_data_path = os.path.join(test_dir_path, 'data/ny_body.txt')
        with open(body_data_path, 'r', encoding='utf-8') as f:
            body = f.read()
        # print("\n\nexpected\n%r\n\nresult\n%r" % (body, self.result.body))
        self.assertEquals(body, self.result.body)
