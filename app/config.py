from crawler import Query, Crawler

class CrawlerDef():

    def __init__(self, label=None, crawler=None, queries=[], download=False,
                 wait_query=None):
        self.label = label
        self.crawler = crawler
        self.queries = queries
        self.download = download
        self.wait_query

crawlers = {
    "ARTICLE": CrawlerDef(
        label="ARTICLE",
        crawler=Crawler,
        queries=[],
        download=True
    ),
    "NY_ARCHIVE": CrawlerDef(
        label="NY_ARCHIVE",
        crawler=Crawler,
        queries=[
            Query(
                query="//li[@class='story noThumb']//a/@href",
                crawler="ARTICLE"
            )
        ],
        download=False,
        wait_query="//li[@class='story noThumb']//a/@href"
    ),
    "DAILY_YEARS": CrawlerDef(
        label="DAILY_YEARS",
        crawler=Crawler,
        queries=[],
        download=False
    ),
    "DAILY_MONTHS": CrawlerDef(
        label="DAILY_MONTHS",
        crawler=Crawler,
        queries=[],
        download=False
    ),
    "DAILY_DAYS": CrawlerDef(
        label="DAILY_DAYS",
        crawler=Crawler,
        queries=[],
        download=False
    ),
}
