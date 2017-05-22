'''
Tests for analyzing and labeling a Moscow Times article
'''
import unittest
import os
import datetime
from app.processor import Processor

test_dir_path = os.path.dirname(__file__)


class TestMoscowTimesProcessing(unittest.TestCase):

    def setUp(self):
        self.maxDiff = 10000
        self.subject = Processor()

        # Given an article page of the Moscow Times
        self.source_url = "https://www.nytimes.com/reuters/2017/05/22/us/politics/22reuters-usa-budget.html"
        test_data_path = os.path.join(test_dir_path, 'data/nytimes_sample.html')
        with open(test_data_path, 'r', encoding='cp1251') as f:
            self.html_data = f.read().replace('\n', '')

    def test_processing(self):

        # When the article is processed by the Processor class
        result = self.subject.process(self.source_url, self.html_data)

        # Then it extracts the article content
        body_data_path = os.path.join(test_dir_path, 'data/ny_body_incorrect.txt')
        with open(body_data_path, 'r', encoding='utf-8') as f:
            self.body = f.read()
        self.assertEquals(self.body, result.body)
        # And its metadata
        expected_title = "Trump Budget Poised to Slash Healthcare for Poor, Other Programs"
        self.assertEquals(expected_title, result.title)
        expected_datetime = datetime.datetime(2017, 5, 22)
        self.assertEquals(expected_datetime, result.datetime)
