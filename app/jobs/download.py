from crawler.storage import PostGresArchiver
from crawler.fetcher import PhantomFetcher
from crawler.fetcher import RequestFetcher


def run(arguments, database=None):
    print("download %r" % arguments)
    url = arguments.get("url")
    source_id = arguments.get("source_id")
    wait_query = arguments.get("wait_query")

    if wait_query is None:
        fetcher = RequestFetcher()
    else:
        fetcher = PhantomFetcher()

    html = fetcher.fetch(url, wait_query)

    print("archiving %s" % url)
    archiver = PostGresArchiver(database)
    archiver.archive(url, html, source_id=source_id)

    result = {
        "url": url,
        "source_id": source_id,
    }
    return [result]
