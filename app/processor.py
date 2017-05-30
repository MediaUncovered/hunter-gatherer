import unicodedata
import datetime
import re
import lxml.html as html
import chardet
from dateutil.parser import parse as parse_date


class Processor(object):

    def __init__(self, title_queries=[], body_queries=[], date_queries=[],
                 date_format=None):
        self.title_queries = title_queries
        self.body_queries = body_queries
        self.date_queries = date_queries
        self.date_format = date_format

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

        date = None
        date_string = self.process_queries(url, tree, self.date_queries)
        if date_string is not None and len(date_string) > 0:
            if self.date_format is not None:
                date = datetime.datetime.strptime(date_string, self.date_format)
            else:
                date = parse_date(date_string)

        return Document(title=title, body=body, date=date)

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

    def __init__(self, title, body, summary=None, date=None):
        self.title = title
        self.body = body
        self.summary = summary
        self.date = date
