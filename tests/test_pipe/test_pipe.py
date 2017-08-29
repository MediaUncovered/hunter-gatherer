'''
Tests if the crawler stores data
'''
import unittest
import unittest.mock
import os
import pipes.pipe as pipe
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
        result = pipe.get_job_definition(self.pipe_definition, job_uuid)

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

    def test_get_next_job_definition(self):
        # When I search for the next job following a job with a specific uuid
        job_uuid = "step3"
        result = pipe.get_next_job_definition(self.pipe_definition, job_uuid)

        # Then it will return its definition
        expected = {
            "uuid": "step4",
            "label": "Moscow Times Article Download",
            "type": "Downloader",
            "arguments": {
                "url": None,
                "source_id": None,
            },
            "queue": "article"
        }
        self.assertEquals(expected, result)
