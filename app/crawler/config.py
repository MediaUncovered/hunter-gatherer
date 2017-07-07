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


class CrawlerDef(object):

    def __init__(self, label=None, crawler=None, queries=[], archive=False,
                 process=False, wait_query=None, version=1, javascript=False,
                 priority=0):
        self.label = label
        self.crawler = crawler
        self.queries = queries
        self.archive = archive
        self.process = process
        self.wait_query = wait_query
        self.version = version
        self.javascript = javascript
        self.priority = priority