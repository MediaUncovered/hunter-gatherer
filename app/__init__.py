import logging


class Query(object):
    '''
    An instruction for how a Crawler should process a page.
    :param query: a string containing a css query, that will result in one or
                  more urls that are to extracted from the page.
    :param crawler: a string with a crawlers label.
    '''

    def __init__(self, query=None, crawler=None):
        self.query = query
        self.crawler = crawler
