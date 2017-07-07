from crawler.config import CrawlerDef, Query
from crawler.crawler import Crawler
from crawler.processor import Processor

crawlers = {
    "ARTICLE_JS": CrawlerDef(
        label="ARTICLE",
        crawler=Crawler,
        queries=[],
        archive=True,
        priority=8
    ),
    "ARTICLE_HTML": CrawlerDef(
        label="ARTICLE",
        crawler=Crawler,
        queries=[],
        archive=True,
        priority=8
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
                crawler="ARTICLE_MOSCOW"
            )
        ],
        archive=False,
        priority=1
    ),
    "ARTICLE_MOSCOW": CrawlerDef(
        label="ARTICLE",
        crawler=Crawler,
        queries=[],
        archive=True,
        process=True,
        priority=8,
    ),
}

processors = {
    "ARTICLE_MOSCOW": Processor(
        title_queries=[Query(query="//div[@class='article_wrap']//h2/text()")],
        body_queries=[Query(query="//div[@class='article_text']//text()")],
        date_queries=[Query(query="//ul[@class='sochi_article_info sochi_article']/li[2]/text()")],
        date_format="%b. %d %Y %H:%M ")
}
