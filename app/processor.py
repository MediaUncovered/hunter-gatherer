import datetime
from lxml import etree


class Processor(object):

    def __init__(self, title_queries=[], body_queries=[],
                 year_queries=[], month_queries=[], date_queries=[]):
        self.title_queries = title_queries
        self.body_queries = body_queries
        self.year_queries = year_queries
        self.month_queries = month_queries
        self.date_queries = date_queries

    def process(self, url, html):
        title = self.process_queries(url, html, self.title_queries)
        body = self.process_queries(url, html, self.body_queries)
        year = self.process_queries(url, html, self.year_queries)
        month = self.process_queries(url, html, self.month_queries)
        date = self.process_queries(url, html, self.date_queries)

        return Document(title=title, body=body)

        # return Document(title=title, body=body,
        #                 datetime=datetime.datetime(year, month, date))

    def process_queries(self, url, html, queries):
        result = ''
        tree = etree.HTML(html)
        for query in queries:
            matches = tree.xpath(query.query)
            for match in matches:
                result += match
        return result


class Document(object):

    def __init__(self, title, body, summary=None, datetime=None):
        self.title = title
        self.body = body
        self.summary = summary
        self.datetime = datetime
