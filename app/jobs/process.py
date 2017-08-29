from crawler import model
from crawler.storage import PostGresArchiver
from crawler.processor import ArticleProcessor


def run(arguments):
    print("process %s" % arguments)
    url = arguments.get("url")
    title_queries = arguments.get("title_queries")
    body_queries = arguments.get("body_queries")
    date_queries = arguments.get("date_queries")
    date_format = arguments.get("date_format")

    session = model.session()
    archiver = PostGresArchiver(session)
    article = archiver.retrieve(url)

    processor = ArticleProcessor(
        title_queries=title_queries,
        body_queries=body_queries,
        date_queries=date_queries,
        date_format=date_format,
    )
    document = processor.process(url, article.html)

    article.title = document.title
    article.body = document.body
    article.published = document.date
    session.commit()
    session.close()

    result = {
        "url": url,
        "title": article.title,
        "body": article.body,
        "published": article.published,
    }
    return [result]
