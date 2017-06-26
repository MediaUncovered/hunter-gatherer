from celery import Celery
from crawler.crawler import Crawler
from crawler.fetcher import RequestFetcher, PhantomFetcher
import jobs.definitions
from kombu import Connection


redis_url = 'redis://result:6379/0'
rabbitmq_url = 'amqp://admin:mypass@queue:5672'

celery_broker_url = rabbitmq_url

broker = Celery('jobs.tasks', broker=celery_broker_url, backend=redis_url)


@broker.task(name="tasks.run_crawler")
def run_crawler(label, url):
    print("running %s %s" % (label, url))
    definition = jobs.definitions.crawlers[label]
    if definition.javascript:
        fetcher = PhantomFetcher()
    else:
        fetcher = RequestFetcher()

    crawler = Crawler(
        definition.queries,
        queuer=Queuer(),
        fetcher=fetcher,
        version=definition.version,
        archive=definition.archive,
        wait_query=definition.wait_query
    )
    crawler.crawl(url)


class Queuer(object):

    def que(self, crawler_label, url):
        print("queueing %s %s" % (crawler_label, url))
        self.ensure_connection()
        run_crawler.delay(crawler_label, url)

    def ensure_connection(self):
        conn = Connection(celery_broker_url)
        conn.ensure_connection(max_retries=10)
