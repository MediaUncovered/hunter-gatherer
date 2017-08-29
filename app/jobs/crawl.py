"""
Runs a Crawler and queues all found urls for the next job in the pipe
"""
from crawler.crawler import Crawler
from crawler.fetcher import PhantomFetcher
from crawler.fetcher import RequestFetcher


def run(arguments):
    print("crawl %s" % arguments)
    url = arguments.get("url")
    queries = arguments.get("queries")
    source_id = arguments.get("source_id")
    wait_query = arguments.get("wait_query")

    if wait_query is None:
        fetcher = RequestFetcher()
    else:
        fetcher = PhantomFetcher()

    print("starting crawler")
    crawler = Crawler(queries, fetcher=fetcher, wait_query=wait_query)
    found_urls = crawler.crawl(url)

    next_arguments = []
    for found_url in found_urls:
        next_arguments.append(
            {
                "url": found_url,
                "source_id": source_id
            }
        )

    return next_arguments
