from celery import Celery
from crawler.crawler import Crawler
import jobs.definitions


redis_url = 'redis://queue:6379/0'
broker = Celery('jobs.tasks', broker=redis_url)


@broker.task(name="tasks.run_crawler")
def run_crawler(label, url):
    print("running %s %s" % (label, url))
    definition = jobs.definitions.crawlers[label]
    crawler = Crawler(
        definition.queries,
        queuer=Queuer(),
        version=definition.version,
        archive=definition.archive,
        wait_query=definition.wait_query
    )
    crawler.crawl(url)

class Queuer(object):

    def que(self, crawler_label, url):
        print("queueing %s %s" % (crawler_label, url))
        run_crawler.delay(crawler_label, url)
