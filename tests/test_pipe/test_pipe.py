'''
Tests the piping mechanisms
'''
import unittest
import unittest.mock
import os
import pipes
import ruamel.yaml as yaml

test_dir_path = os.path.dirname(__file__)


class TestPipe(unittest.TestCase):

    def setUp(self):
        # Given I have a pipe definition
        pipe_definition_path = os.path.join(
            test_dir_path,
            "data/moscow_times_archive.yml"
        )
        with open(pipe_definition_path) as stream:
            pipe_definition = yaml.load(stream, Loader=yaml.Loader)
        self.pipe_definition = pipe_definition

    def test_get_job_definition(self):
        # When I search for a job with a specific uuid
        job_uuid = "step3"
        result = pipes.get_job_definition(self.pipe_definition, job_uuid)

        # Then it will return its definition
        expected = {
            "uuid": "step3",
            "label": "Moscow Times Day",
            "type": "Crawler",
            "arguments": {
                "url": None,
                "query": "//div[@class='content']/div[@class='left']//a/@href",
                "source_id": None,
            },
            "queue": "archive"
        }
        self.assertEquals(expected, result)

    def test_get_next_job_definitions(self):
        # When I search for the next job following a job with a specific uuid
        job_uuid = "step3"
        result = pipes.get_next_job_definitions(self.pipe_definition, job_uuid)

        # Then it will return its definitions
        expected = [
            {
                "uuid": "step4",
                "label": "Moscow Times Article Download",
                "type": "Downloader",
                "arguments": {
                    "url": None,
                    "source_id": None,
                },
                "queue": "article"
            }
        ]
        self.assertEquals(expected, result)


class TestPipeRecursive(unittest.TestCase):

    def setUp(self):
        # Given I have a pipe definition
        pipe_definition_path = os.path.join(
            test_dir_path,
            "data/ny_times_archive.yml"
        )
        with open(pipe_definition_path) as stream:
            pipe_definition = yaml.load(stream, Loader=yaml.Loader)
        self.pipe_definition = pipe_definition

    def test_get_next_job_definitions_including_recursive(self):
        # When I search for the next job following a job with a specific uuid
        job_uuid = "step1"
        result = pipes.get_next_job_definitions(self.pipe_definition, job_uuid, include_recusive=True)

        # Then it will return its definitions
        expected = [
            {
                "uuid": "step2",
                "label": "NY Times Archive Page",
                "type": "Crawler",
                "arguments": {
                    "url": None,
                    "query": "//li[@class='story noThumb']//a/@href",
                    "source_id": None,
                },
                "queue": "crawler"
            },
            {
                "uuid": "step1",
                "label": "NY Times Archive upper",
                "type": "Pager",
                "recursive": True,
                "arguments": {
                    "pager_pattern": "https://query.nytimes.com/search/sitesearch/#/*/from19810101to20171231/document_type%3A%22article%22/{page}/allauthors/oldest/",
                    "pager_page": 1,
                    "source_id": 1,
                },
                "queue": "crawler"
            }
        ]
        self.assertEquals(expected, result)

    def test_get_next_job_definitions_excluding_recursive(self):
        # When I search for the next job following a job with a specific uuid
        job_uuid = "step1"
        result = pipes.get_next_job_definitions(self.pipe_definition, job_uuid, include_recusive=False)

        # Then it will return its definitions
        expected = [
            {
                "uuid": "step2",
                "label": "NY Times Archive Page",
                "type": "Crawler",
                "arguments": {
                    "url": None,
                    "query": "//li[@class='story noThumb']//a/@href",
                    "source_id": None,
                },
                "queue": "crawler"
            }
        ]
        self.assertEquals(expected, result)
