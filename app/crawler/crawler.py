'''
Crawls an XML/HTML document. It can extract urls for further crawling and
optionally store the documents it has visited.
'''
from lxml import etree
from crawler.fetcher import PhantomFetcher
import urllib.parse as urlparse


class Crawler(object):
    '''
    Crawls a page and returns a set of urls, depending on the queries
    configured.
    :param queries: an array of Query objects, configuring the Crawler.
    :param fetcher: an implementation of Fetcher.
    :param wait_query: an xpath query that must first produce at least one
                       match, before the page is used for url extraction. This
                       allows pages that use javascript to be crawled.
    '''

    def __init__(self, queries,
                 fetcher=PhantomFetcher(),
                 wait_query=None):
        self.queries = queries
        self.wait_query = wait_query
        self.fetcher = fetcher

    '''
    Fetches the given url with the configured Fetcher and applies the queries
    to the body of the response.
    :param url: a url resulting in the html to be crawled
    :returns: A list of matches for the configured queries.
    '''
    def crawl(self, url):
        print("fetching %s" % url)
        html = self.fetcher.fetch(url, self.wait_query)

        print("extracting queries")
        urls = self.extract(url, html, self.queries)

        return urls

    def extract(self, original_url, html, queries):
        tree = etree.HTML(html)
        found_urls = []
        for query in queries:
            urls = tree.xpath(query)
            for url in urls:
                joined_url = urlparse.urljoin(original_url, url)
                found_urls.append(
                    joined_url
                )
        return found_urls
