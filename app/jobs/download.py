from crawler import model
from crawler.storage import PostGresArchiver
from crawler.fetcher import PhantomFetcher
from crawler.fetcher import RequestFetcher


def run(arguments):
    print("download %s" % arguments)
    url = arguments.get("url")
    source_id = arguments.get("source_id")
    wait_query = arguments.get("wait_query")

    if wait_query is None:
        fetcher = RequestFetcher()
    else:
        fetcher = PhantomFetcher()

    html = fetcher.fetch(url, wait_query)

    print("archiving %s" % url)
    session = model.session()
    archiver = PostGresArchiver(session)
    archiver.archive(url, html, source_id=source_id)

    result = {
        "url": url,
        "source_id": source_id,
    }
    return [result]
