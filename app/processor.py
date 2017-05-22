from newspaper import Article

class Archiver(object):

    def archive(self, url, html):
        raise Exception("TODO implement")


class Processor(object):

    def process(self, url, html):
        article = Article(url)
        article.set_html(html)
        article.parse()

        return Document(title=article.title, body=article.text,
                        summary=article.summary, datetime=article.publish_date)


class Document(object):

    def __init__(self, title, body, summary=None, datetime=None):
        self.title = title
        self.body = body
        self.summary = summary
        self.datetime = datetime
