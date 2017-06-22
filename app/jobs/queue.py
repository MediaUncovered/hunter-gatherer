from jobs.tasks import run_crawler

class Order(object):
    '''
    Describes an Order to crawl an url with a specific crawler. It can be
    stored in a datastore and converted into a Job by a JobRunner.
    '''

    def __init__(self, url, crawler_label):
        self.url = url
        self.crawler_label = crawler_label


class Queuer(object):

    def queue(self, order):
        run_crawler.delay("NY_ARCHIVE", "some url")
        # TODO store the Order in the datastore
