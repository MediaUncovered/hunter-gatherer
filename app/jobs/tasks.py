import os
from celery import Celery
from crawler.crawler import Crawler
from crawler.fetcher import RequestFetcher, PhantomFetcher
from crawler.storage import PostGresArchiver
import crawler.model as model
import jobs.definitions
from kombu import Connection

redis_host = os.environ["RESULT_HOST"]
redis_port = os.environ["RESULT_PORT"]  # 6379
redis_url = 'redis://%s:%s/0' % (
    redis_host,
    redis_port,
)

rabbitmq_user = os.environ["QUEUE_USER"]
rabbitmq_password = os.environ["QUEUE_PASSWORD"]
rabbitmq_host = os.environ["QUEUE_HOST"]
rabbitmq_port = os.environ["QUEUE_PORT"]  # 5672
rabbitmq_url = 'amqp://%s:%s@%s:%s' % (
    rabbitmq_user,
    rabbitmq_password,
    rabbitmq_host,
    rabbitmq_port
)

celery_broker_url = rabbitmq_url

broker = Celery('jobs.tasks', broker=celery_broker_url, backend=redis_url)


@broker.task(name="tasks.run_crawler", autoretry_for=(Exception,),
             retry_kwargs={'max_retries': 5})
def run_crawler(label, url, source_id):
    print("running %s %s" % (label, url))
    definition = jobs.definitions.crawlers[label]
    if definition.javascript:
        fetcher = PhantomFetcher()
    else:
        fetcher = RequestFetcher()
    session = model.session()

    queuer = Queuer()

    crawler = Crawler(
        definition.queries,
        queuer=queuer,
        fetcher=fetcher,
        archiver=PostGresArchiver(session),
        version=definition.version,
        archive=definition.archive,
        wait_query=definition.wait_query
    )
    crawler.crawl(url, source_id=source_id)

    session.close()

    if definition.process:
        queuer.que_processing(label, url, priority=9)


@broker.task(name="tasks.run_processor", autoretry_for=(Exception,),
             retry_kwargs={'max_retries': 5})
def run_processor(label, url):
    session = model.session()
    archiver = PostGresArchiver(session)
    article = archiver.retrieve(url)

    processor = jobs.definitions.processors[label]
    document = processor.process(url, article.html)

    article.title = document.title
    article.body = document.body
    article.published = document.date
    session.commit()
    session.close()


class Queuer(object):

    def que(self, crawler_label, url, source_id, priority=0):
        print("queueing crawling %s %s %d" % (crawler_label, url, source_id))
        self.ensure_connection()
        run_crawler.apply_async(args=(crawler_label, url, source_id), priority=priority)

    def que_processing(self, processor_label, url, priority=9):
        print("queueing processing %s %s" % (processor_label, url))
        self.ensure_connection()
        run_processor.apply_async(args=(processor_label, url), priority=priority)

    def ensure_connection(self):
        conn = Connection(celery_broker_url)
        conn.ensure_connection(max_retries=10)
