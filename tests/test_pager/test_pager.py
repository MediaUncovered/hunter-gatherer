'''
Tests the recursive pager plugin
'''
import unittest
import app.jobs.pager as pager


class TestPager(unittest.TestCase):

    def test_ny1(self):

        args = {
            "pager_pattern": "https://query.nytimes.com/search/sitesearch/#/*/from19810101to20171231/document_type%3A%22article%22/{page}/allauthors/oldest/",
            "pager_page": 1,
            "source_id": 1,
        }
        result = pager.run(args)

        expected = {
            "pager_pattern": "https://query.nytimes.com/search/sitesearch/#/*/from19810101to20171231/document_type%3A%22article%22/{page}/allauthors/oldest/",
            "pager_page": 2,
            "url": "https://query.nytimes.com/search/sitesearch/#/*/from19810101to20171231/document_type%3A%22article%22/1/allauthors/oldest/",
        }

        self.assertEquals(expected, result)

    def test_ny2(self):

        args = {
            "pager_pattern": "https://query.nytimes.com/search/sitesearch/#/*/from19810101to20171231/document_type%3A%22article%22/{page}/allauthors/oldest/",
            "pager_page": 5,
            "source_id": 1,

        }
        result = pager.run(args)

        expected = {
            "pager_pattern": "https://query.nytimes.com/search/sitesearch/#/*/from19810101to20171231/document_type%3A%22article%22/{page}/allauthors/oldest/",
            "pager_page": 6,
            "url": "https://query.nytimes.com/search/sitesearch/#/*/from19810101to20171231/document_type%3A%22article%22/5/allauthors/oldest/",
        }

        self.assertEquals(expected, result)
