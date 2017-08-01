import logging
from crawler.model import Article


class Archiver(object):

    def archive(self, url, html, source_id=None):
        raise Exception("TODO implement")


class PostGresArchiver(Archiver):

    def __init__(self, session):
        self.session = session

    def archive(self, url, html, source_id=None):
        article = self.retrieve(url)
        if article is None:
            article = Article()
            self.session.add(article)

        article.url = url
        article.html = html
        article.source_id = source_id
        
        self.session.commit()
        return article

    def retrieve(self, url):
        article = self.session.query(Article).filter(Article.url == url).one()
        if article is None:
            print("article for url %s not found" % url)
        else:
            print("found article.id %d for url %s" % (article.id, url))
        return article

    def all(self):
        articles = self.session.query(Article)
        return articles
