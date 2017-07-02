'''
Tests for the Moscow times crawlers
'''
import unittest
import os
from crawler.config import Query
from crawler.crawler import Crawler

test_dir_path = os.path.dirname(__file__)


class MockFetcher():
    def __init__(self, page_source):
        self.page_source = page_source

    def fetch(self, url, wait_query):
        return self.page_source


class MockQueuer():

    def __init__(self):
        self.orders = []

    def que(self, crawler_label, url, priority=0):
        self.orders.append((crawler_label, url))


class TestAllCrawling(unittest.TestCase):

    def setUp(self):
        # Given an archive page of the NY Times
        test_data_path = os.path.join(test_dir_path, 'data/themoscowtimes_all_sample.html')
        with open(test_data_path, 'r', encoding='cp1251') as f:
            self.html_data = f.read().replace('\n', '')
        # And a Crawler configured to extract article urls
        self.queries = [
            Query(
                query="//div[@class='block_left']//a/@href",
                crawler="MOSCOW_YEAR"
            )
        ]

    def test_extraction(self):
        crawler = Crawler(
            self.queries,
            fetcher=MockFetcher(self.html_data),
            queuer=MockQueuer()
        )

        # When the crawler extracts data from the archive page
        test_url = "http://old.themoscowtimes.com/sitemap/"
        crawler.crawl(test_url)

        # Then it will have queued the Orders
        expected = [
            ("MOSCOW_YEAR", "http://old.themoscowtimes.com/sitemap/free/2017.html"),
            ("MOSCOW_YEAR", "http://old.themoscowtimes.com/sitemap/free/2016.html"),
            ("MOSCOW_YEAR", "http://old.themoscowtimes.com/sitemap/free/2015.html"),
            ("MOSCOW_YEAR", "http://old.themoscowtimes.com/sitemap/free/2014.html"),
            ("MOSCOW_YEAR", "http://old.themoscowtimes.com/sitemap/free/2013.html"),
            ("MOSCOW_YEAR", "http://old.themoscowtimes.com/sitemap/free/2012.html"),
            ("MOSCOW_YEAR", "http://old.themoscowtimes.com/sitemap/free/2011.html"),
            ("MOSCOW_YEAR", "http://old.themoscowtimes.com/sitemap/free/2010.html"),
            ("MOSCOW_YEAR", "http://old.themoscowtimes.com/sitemap/free/2009.html"),
            ("MOSCOW_YEAR", "http://old.themoscowtimes.com/sitemap/free/2008.html"),
            ("MOSCOW_YEAR", "http://old.themoscowtimes.com/sitemap/free/2007.html"),
            ("MOSCOW_YEAR", "http://old.themoscowtimes.com/sitemap/free/2006.html"),
            ("MOSCOW_YEAR", "http://old.themoscowtimes.com/sitemap/free/2005.html"),
            ("MOSCOW_YEAR", "http://old.themoscowtimes.com/sitemap/free/2004.html"),
            ("MOSCOW_YEAR", "http://old.themoscowtimes.com/sitemap/free/2003.html"),
            ("MOSCOW_YEAR", "http://old.themoscowtimes.com/sitemap/free/2002.html"),
            ("MOSCOW_YEAR", "http://old.themoscowtimes.com/sitemap/free/2001.html"),
            ("MOSCOW_YEAR", "http://old.themoscowtimes.com/sitemap/free/2000.html"),
            ("MOSCOW_YEAR", "http://old.themoscowtimes.com/sitemap/free/1999.html"),
            ("MOSCOW_YEAR", "http://old.themoscowtimes.com/sitemap/free/1998.html"),
            ("MOSCOW_YEAR", "http://old.themoscowtimes.com/sitemap/free/1997.html"),
            ("MOSCOW_YEAR", "http://old.themoscowtimes.com/sitemap/free/1996.html"),
            ("MOSCOW_YEAR", "http://old.themoscowtimes.com/sitemap/free/1995.html"),
            ("MOSCOW_YEAR", "http://old.themoscowtimes.com/sitemap/free/1994.html"),
            ("MOSCOW_YEAR", "http://old.themoscowtimes.com/sitemap/free/1993.html"),
            ("MOSCOW_YEAR", "http://old.themoscowtimes.com/sitemap/free/1992.html")
        ]
        self.assertEquals(len(expected), len(crawler.queuer.orders))
        for index, expected_order in enumerate(expected):
            result_order = crawler.queuer.orders[index]
            self.assertEquals(expected_order, result_order)


class TestYearCrawling(unittest.TestCase):

    def setUp(self):
        # Given a year page of the moscow times
        test_data_path = os.path.join(test_dir_path, 'data/themoscowtimes_year_sample.html')
        with open(test_data_path, 'r', encoding='cp1251') as f:
            self.html_data = f.read().replace('\n', '')
        # And a Crawler configured to extract article urls
        self.queries = [
            Query(
                query="//div[@class='sitemap_calend']//a/@href",
                crawler="MOSCOW_DAY"
            )
        ]

    def test_extraction(self):
        crawler = Crawler(
            self.queries,
            fetcher=MockFetcher(self.html_data),
            queuer=MockQueuer()
        )

        # When the crawler extracts data from the archive page
        test_url = "http://old.themoscowtimes.com/sitemap/free/1992.html"
        crawler.crawl(test_url)

        # Then it will have queued the Orders
        expected = [
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/3/6.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/3/10.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/3/13.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/3/17.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/3/20.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/3/24.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/3/27.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/3/31.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/4/3.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/4/10.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/4/14.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/4/17.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/4/21.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/4/24.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/4/28.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/4/30.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/5/6.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/5/8.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/5/13.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/5/15.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/5/19.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/5/22.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/5/26.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/5/29.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/6/2.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/6/5.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/6/9.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/6/12.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/6/16.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/6/19.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/6/26.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/6/30.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/7/3.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/7/4.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/7/7.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/7/10.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/7/14.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/7/17.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/7/21.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/7/23.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/7/24.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/7/28.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/7/31.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/8/4.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/8/7.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/8/11.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/8/14.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/8/18.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/8/21.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/8/25.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/8/28.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/9/4.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/9/8.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/9/11.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/9/15.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/9/18.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/9/22.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/9/25.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/9/29.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/10/2.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/10/5.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/10/6.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/10/7.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/10/8.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/10/9.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/10/12.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/10/13.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/10/14.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/10/15.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/10/16.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/10/19.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/10/20.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/10/21.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/10/22.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/10/23.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/10/26.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/10/27.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/10/28.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/10/29.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/10/30.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/11/2.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/11/3.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/11/4.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/11/5.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/11/6.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/11/10.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/11/11.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/11/12.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/11/13.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/11/16.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/11/17.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/11/18.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/11/19.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/11/20.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/11/23.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/11/24.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/11/25.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/11/26.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/11/27.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/11/29.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/11/30.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/12/1.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/12/2.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/12/3.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/12/4.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/12/7.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/12/8.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/12/9.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/12/10.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/12/11.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/12/14.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/12/15.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/12/16.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/12/17.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/12/18.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/12/21.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/12/22.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/12/23.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/12/29.html"),
             ("MOSCOW_DAY", "http://old.themoscowtimes.com/sitemap/free/1992/12/30.html")
        ]

        self.assertEquals(len(expected), len(crawler.queuer.orders))
        for index, expected_order in enumerate(expected):
            result_order = crawler.queuer.orders[index]
            self.assertEquals(expected_order, result_order)


class TestDayCrawling(unittest.TestCase):

    def setUp(self):
        # Given an archive page of the NY Times
        test_data_path = os.path.join(test_dir_path, 'data/themoscowtimes_day_sample.html')
        with open(test_data_path, 'r', encoding='cp1251') as f:
            self.html_data = f.read().replace('\n', '')
        # And a Crawler configured to extract article urls
        self.queries = [
            Query(
                query="//div[@class='content']/div[@class='left']//a/@href",
                crawler="ARTICLE"
            )
        ]

    def test_extraction(self):
        crawler = Crawler(
            self.queries,
            fetcher=MockFetcher(self.html_data),
            queuer=MockQueuer()
        )

        # When the crawler extracts data from the archive page
        test_url = "http://old.themoscowtimes.com/sitemap/free/1992/5/8.html"
        crawler.crawl(test_url)

        # Then it will have queued the Orders
        expected = [
            ("ARTICLE", "http://old.themoscowtimes.com/sitemap/free/1992/5/article/american-was-assassinated-family-says/221589.html"),
            ("ARTICLE", "http://old.themoscowtimes.com/sitemap/free/1992/5/article/pepsi-to-save-vodka-cola-deal/221588.html"),
            ("ARTICLE", "http://old.themoscowtimes.com/sitemap/free/1992/5/article/soviet-trucks-to-roll-westwards/221587.html"),
            ("ARTICLE", "http://old.themoscowtimes.com/sitemap/free/1992/5/article/british-womens-club-formed/221586.html"),
            ("ARTICLE", "http://old.themoscowtimes.com/sitemap/free/1992/5/article/yacht-club-launches-lessons-and-cruises/221585.html"),
            ("ARTICLE", "http://old.themoscowtimes.com/sitemap/free/1992/5/article/top-yeltsin-advisor-asks-to-step-down/221584.html"),
            ("ARTICLE", "http://old.themoscowtimes.com/sitemap/free/1992/5/article/birthday-magic/221583.html"),
            ("ARTICLE", "http://old.themoscowtimes.com/sitemap/free/1992/5/article/russians-clash-with-u-s-on-nuclear-arms-control/221582.html"),
            ("ARTICLE", "http://old.themoscowtimes.com/sitemap/free/1992/5/article/health-workers-strike-threatens-government/221581.html"),
            ("ARTICLE", "http://old.themoscowtimes.com/sitemap/free/1992/5/article/vodka-price-hikes-unlikely-to-effect-drinking-habits/221580.html"),
            ("ARTICLE", "http://old.themoscowtimes.com/sitemap/free/1992/5/article/firm-denies-finding-cpsu-billions/221579.html"),
            ("ARTICLE", "http://old.themoscowtimes.com/sitemap/free/1992/5/article/secret-archives-just-a-peek/221578.html"),
            ("ARTICLE", "http://old.themoscowtimes.com/sitemap/free/1992/5/article/tretyakov-promised-15-million/221577.html"),
            ("ARTICLE", "http://old.themoscowtimes.com/sitemap/free/1992/5/article/victory-day-festivities/221576.html"),
            ("ARTICLE", "http://old.themoscowtimes.com/sitemap/free/1992/5/article/communists-fights-back/221575.html"),
            ("ARTICLE", "http://old.themoscowtimes.com/sitemap/free/1992/5/article/jack-the-ripper-sentenced-to-death/221574.html"),
            ("ARTICLE", "http://old.themoscowtimes.com/sitemap/free/1992/5/article/corpses-crowd-city-morgues/221573.html"),
            ("ARTICLE", "http://old.themoscowtimes.com/sitemap/free/1992/5/article/ex-spy-blake-calls-chocolate-cake-reports-rubbish/221572.html"),
            ("ARTICLE", "http://old.themoscowtimes.com/sitemap/free/1992/5/article/asylum-seeking-north-korean-under-siege/221571.html"),
            ("ARTICLE", "http://old.themoscowtimes.com/sitemap/free/1992/5/article/the-man-who-would-be-president/221570.html"),
            ("ARTICLE", "http://old.themoscowtimes.com/sitemap/free/1992/5/article/teen-mafia-rules-moscow-streets/221569.html"),
            ("ARTICLE", "http://old.themoscowtimes.com/sitemap/free/1992/5/article/opposition-forces-oust-tajik-president/221568.html"),
            ("ARTICLE", "http://old.themoscowtimes.com/sitemap/free/1992/5/article/august-1-convertible-ruble-a-long-shot-bet/221567.html")
        ]
        self.assertEquals(len(expected), len(crawler.queuer.orders))
        for index, expected_order in enumerate(expected):
            result_order = crawler.queuer.orders[index]
            self.assertEquals(expected_order, result_order)
