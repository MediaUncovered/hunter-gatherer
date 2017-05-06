'''
Crawls an archive page of a newspaper. It stores the page, extracts urls of
articles and the url of the next page in the archive.
'''
import logging
import requests


class Page():
    '''
    A result object for an archive crawl.
    '''

    def __init__(self, article_urls, next_page_url):
        self.article_urls = article_urls
        self.next_page_url = next_page_url


class Config():
    '''
    For storing crawler configs into databases and translating between the two
    (the database and Python) formats. This allows for easier multithreaded
    article extraction.
    '''
    def __init__(self, newspaper_id=None, newspaper_name=None, article_css=None,
                 next_page_css=None):
        self.newspaper_id = newspaper_id
        self.newspaper_name = newspaper_name
        self.article_css = article_css
        self.next_page_css = next_page_css


class Crawler():
    '''
    Crawls an archive page and stores its results in a datastore to await
    processing
    '''

    def __init__(self, newspaper_id=None, newspaper_name=None, article_css=None,
                 next_page_css=None, version=1):
        self.newspaper_id = newspaper_id
        self.newspaper_name = newspaper_name
        self.article_css = article_css
        self.next_page_css = next_page_css

        # in case we want to reprocess some urls with a different extraction
        self.version = version

    def crawl(self, archive_url):
        req = requests.get(archive_url)
        page = self.__extract(req.text)
        self.__store(page)

    def extract(self, html_text):
        raise Exception("TODO implement")
        page = Page()
        # TODO use the css to get all the urls needed from the page and store them in the Page object
        # TODO use the css to get the next url needed from the page and store it in the Page object
        return page

    def store(self, page):
        logging.warning("Storing archive pages isn't implemented yet")
        # TODO store the page in the datastore
