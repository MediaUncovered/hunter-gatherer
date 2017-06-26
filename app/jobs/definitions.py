from crawler.config import CrawlerDef, Query
from crawler.crawler import Crawler

crawlers = {
    "ARTICLE_JS": CrawlerDef(
        label="ARTICLE",
        crawler=Crawler,
        queries=[],
        archive=True
    ),
    "ARTICLE_HTML": CrawlerDef(
        label="ARTICLE",
        crawler=Crawler,
        queries=[],
        archive=True
    ),
    "NY_ARCHIVE": CrawlerDef(
        label="NY_ARCHIVE",
        crawler=Crawler,
        queries=[
            Query(
                query="//li[@class='story noThumb']//a/@href",
                crawler="ARTICLE_JS"
            )
        ],
        archive=False,
        wait_query="//li[@class='story noThumb']//a/@href",
        javascript=True
    ),
    "MOSCOW_ALL": CrawlerDef(
        label="MOSCOW_ALL",
        crawler=Crawler,
        queries=[
            Query(
                query="//div[@class='block_left']//a/@href",
                crawler="MOSCOW_YEAR"
            )
        ],
        archive=False
    ),
    "MOSCOW_YEAR": CrawlerDef(
        label="MOSCOW_YEAR",
        crawler=Crawler,
        queries=[
            Query(
                query="//div[@class='sitemap_calend']//a/@href",
                crawler="MOSCOW_DAY"
            )
        ],
        archive=False
    ),
    "MOSCOW_DAY": CrawlerDef(
        label="MOSCOW_DAY",
        crawler=Crawler,
        queries=[
            Query(
                query="//div[@class='content']/div[@class='left']//a/@href",
                crawler="ARTICLE_HTML"
            )
        ],
        archive=False
    ),
}
