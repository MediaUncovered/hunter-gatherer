'''
Crawls an XML/HTML document. It can extract urls for further crawling and
optionally store the documents it has visited.
'''
from lxml import etree
import urllib.parse as urlparse
from jsonpath_rw import parse as parse_json_path
import json


class Crawler(object):
    '''
    Crawls a page and returns a set of urls, depending on the paths
    configured.
    :param xpaths: an array of xpaths, describing a path to an url.
    :param jsonpaths: an array of xpaths, describing a jsonpaths to an url.
    :param fetcher: an implementation of Fetcher.
    :param wait_query: an xpath query that must first produce at least one
                       match, before the page is used for url extraction. This
                       allows pages that use javascript to be crawled.
    '''

    def __init__(self, xpaths=[], jsonpaths=[],
                 fetcher=None,
                 wait_query=None):
        self.xpaths = xpaths
        self.jsonpaths = jsonpaths
        self.wait_query = wait_query
        self.fetcher = fetcher

    '''
    Fetches the given url with the configured Fetcher and applies the xpaths
    to the body of the response.
    :param url: a url resulting in the html to be crawled
    :returns: A list of matches for the configured xpaths.
    '''
    def crawl(self, url):
        print("fetching %s" % url)
        body = self.fetcher.fetch(url, self.wait_query)

        xpath_urls = self.extract_xpaths(url, body, self.xpaths)
        jsonpath_urls = self.extract_jsonpaths(url, body, self.jsonpaths)

        return xpath_urls + jsonpath_urls

    def extract_xpaths(self, original_url, body, xpaths):
        found_urls = []
        if xpaths is not None and len(xpaths) > 0:
            print("extracting xpaths")
            tree = etree.HTML(body)
            for path in xpaths:
                urls = tree.xpath(path)
                for url in urls:
                    joined_url = urlparse.urljoin(original_url, url)
                    found_urls.append(
                        joined_url
                    )
        return found_urls

    def extract_jsonpaths(self, original_url, body, jsonpaths):
        found_urls = []
        if jsonpaths is not None and len(jsonpaths) > 0:
            print("extracting jsonpaths")
            for path in jsonpaths:
                expression = parse_json_path(path)
                json_string = body.decode("utf8")
                json_object = json.loads(json_string)
                urls = [match.value for match in expression.find(json_object)]
                for url in urls:
                    joined_url = urlparse.urljoin(original_url, url)
                    found_urls.append(
                        joined_url
                    )
        return found_urls
