'''
Tests the recursive paginate plugin
'''
import unittest
import app.jobs.paginate as paginate


class TestPagination(unittest.TestCase):

    def test_ny1(self):

        args = {
            "paginate_pattern": "https://query.nytimes.com/search/sitesearch/#/*/from19810101to20171231/document_type%3A%22article%22/{page}/allauthors/oldest/",
            "paginate_page": 1,
            "source_id": 1,
        }
        ended, result = paginate.run(args)

        expected = [{
            "paginate_pattern": "https://query.nytimes.com/search/sitesearch/#/*/from19810101to20171231/document_type%3A%22article%22/{page}/allauthors/oldest/",
            "paginate_page": 2,
            "url": "https://query.nytimes.com/search/sitesearch/#/*/from19810101to20171231/document_type%3A%22article%22/1/allauthors/oldest/",
            "source_id": 1,
        }]

        self.assertEquals(expected, result)

    def test_ny2(self):

        args = {
            "paginate_pattern": "https://query.nytimes.com/search/sitesearch/#/*/from19810101to20171231/document_type%3A%22article%22/{page}/allauthors/oldest/",
            "paginate_page": 5,
            "source_id": 1,

        }
        ended, result = paginate.run(args)

        expected = [{
            "paginate_pattern": "https://query.nytimes.com/search/sitesearch/#/*/from19810101to20171231/document_type%3A%22article%22/{page}/allauthors/oldest/",
            "paginate_page": 6,
            "url": "https://query.nytimes.com/search/sitesearch/#/*/from19810101to20171231/document_type%3A%22article%22/5/allauthors/oldest/",
            "source_id": 1,
        }]

        self.assertEquals(expected, result)
