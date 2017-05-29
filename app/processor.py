import unicodedata
import re
import lxml.html as html
import chardet


class Processor(object):

    def __init__(self, title_queries=[], body_queries=[],
                 year_queries=[], month_queries=[], date_queries=[]):
        self.title_queries = title_queries
        self.body_queries = body_queries
        self.year_queries = year_queries
        self.month_queries = month_queries
        self.date_queries = date_queries

    def process(self, url, html_binary, encoding=None):
        if encoding is None:
            encoding = chardet.detect(html_binary)['encoding']
        if encoding == "utf-8":
            html_string = html_binary.decode("utf-8")
        else:
            html_string = html_binary.decode(encoding).encode("utf-8")

        tree = html.fromstring(html_string)

        title = self.process_queries(url, tree, self.title_queries)
        body = self.process_queries(url, tree, self.body_queries)
        year = self.process_queries(url, tree, self.year_queries)
        month = self.process_queries(url, tree, self.month_queries)
        date = self.process_queries(url, tree, self.date_queries)

        return Document(title=title, body=body)

    def process_queries(self, url, tree, queries):
        result = b''
        space = " ".encode("utf-8")
        for query in queries:
            matches = tree.xpath(query.query)
            for match in matches:
                encoded = str(match).encode("utf-8")
                if len(result) > 0:
                    result += space
                result += encoded

        normalized = unicodedata.normalize("NFKD", result.decode("utf-8"))
        normalized = re.sub(' +', ' ', normalized)
        return normalized


class Document(object):

    def __init__(self, title, body, summary=None, datetime=None):
        self.title = title
        self.body = body
        self.summary = summary
        self.datetime = datetime
