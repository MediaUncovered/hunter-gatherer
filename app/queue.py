class Order(object):
    '''
    Describes an Order to crawl an url with a specific crawler. It can be
    stored in a datastore and converted into a Job by a JobRunner.
    '''

    def __init__(self, url, crawler_label):
        self.url = url
        self.crawler_label = crawler_label
