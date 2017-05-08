class Order():
    '''
    Describes an Order to crawl an url with a specific crawler. It can be
    stored in a datastore and converted into a Job by a JobRunner.
    '''

    def __init__(self, url, crawler):
        self.url = url
        self.crawler = crawler


def queue(order):
    logging.warning("queing Orders isn't implemented yet")
    # TODO store the Order in the datastore
