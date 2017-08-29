'''
Tests for the Moscow times crawlers
'''
import unittest
import os
from crawler.crawler import Crawler

test_dir_path = os.path.dirname(__file__)


class MockFetcher():
    def __init__(self, page_source):
        self.page_source = page_source

    def fetch(self, url, wait_query):
        return self.page_source


class TestAllCrawling(unittest.TestCase):

    def setUp(self):
        # Given an archive page of the NY Times
        test_data_path = os.path.join(test_dir_path, 'data/themoscowtimes_all_sample.html')
        with open(test_data_path, 'r', encoding='cp1251') as f:
            self.html_data = f.read().replace('\n', '')
        # And a Crawler configured to extract article urls
        self.queries = [
            "//div[@class='block_left']//a/@href",
        ]

    def test_extraction(self):
        crawler = Crawler(
            self.queries,
            fetcher=MockFetcher(self.html_data)
        )

        # When the crawler extracts data from the archive page
        test_url = "http://old.themoscowtimes.com/sitemap/"
        result = crawler.crawl(test_url)

        # Then it will have found the year urls
        expected = [
            "http://old.themoscowtimes.com/sitemap/free/2017.html",
            "http://old.themoscowtimes.com/sitemap/free/2016.html",
            "http://old.themoscowtimes.com/sitemap/free/2015.html",
            "http://old.themoscowtimes.com/sitemap/free/2014.html",
            "http://old.themoscowtimes.com/sitemap/free/2013.html",
            "http://old.themoscowtimes.com/sitemap/free/2012.html",
            "http://old.themoscowtimes.com/sitemap/free/2011.html",
            "http://old.themoscowtimes.com/sitemap/free/2010.html",
            "http://old.themoscowtimes.com/sitemap/free/2009.html",
            "http://old.themoscowtimes.com/sitemap/free/2008.html",
            "http://old.themoscowtimes.com/sitemap/free/2007.html",
            "http://old.themoscowtimes.com/sitemap/free/2006.html",
            "http://old.themoscowtimes.com/sitemap/free/2005.html",
            "http://old.themoscowtimes.com/sitemap/free/2004.html",
            "http://old.themoscowtimes.com/sitemap/free/2003.html",
            "http://old.themoscowtimes.com/sitemap/free/2002.html",
            "http://old.themoscowtimes.com/sitemap/free/2001.html",
            "http://old.themoscowtimes.com/sitemap/free/2000.html",
            "http://old.themoscowtimes.com/sitemap/free/1999.html",
            "http://old.themoscowtimes.com/sitemap/free/1998.html",
            "http://old.themoscowtimes.com/sitemap/free/1997.html",
            "http://old.themoscowtimes.com/sitemap/free/1996.html",
            "http://old.themoscowtimes.com/sitemap/free/1995.html",
            "http://old.themoscowtimes.com/sitemap/free/1994.html",
            "http://old.themoscowtimes.com/sitemap/free/1993.html",
            "http://old.themoscowtimes.com/sitemap/free/1992.html",
        ]
        self.assertEquals(len(expected), len(result))
        for index, expected_url in enumerate(expected):
            result_url = result[index]
            self.assertEquals(expected_url, result_url)


class TestYearCrawling(unittest.TestCase):

    def setUp(self):
        # Given a year page of the moscow times
        test_data_path = os.path.join(test_dir_path, 'data/themoscowtimes_year_sample.html')
        with open(test_data_path, 'r', encoding='cp1251') as f:
            self.html_data = f.read().replace('\n', '')
        # And a Crawler configured to extract article urls
        self.queries = [
            "//div[@class='sitemap_calend']//a/@href",
        ]

    def test_extraction(self):
        crawler = Crawler(
            self.queries,
            fetcher=MockFetcher(self.html_data)
        )

        # When the crawler extracts data from the archive page
        test_url = "http://old.themoscowtimes.com/sitemap/free/1992.html"
        result = crawler.crawl(test_url)

        # Then it will have found the day urls
        expected = [
            "http://old.themoscowtimes.com/sitemap/free/1992/3/6.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/3/10.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/3/13.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/3/17.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/3/20.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/3/24.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/3/27.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/3/31.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/4/3.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/4/10.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/4/14.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/4/17.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/4/21.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/4/24.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/4/28.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/4/30.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/5/6.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/5/8.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/5/13.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/5/15.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/5/19.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/5/22.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/5/26.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/5/29.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/6/2.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/6/5.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/6/9.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/6/12.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/6/16.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/6/19.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/6/26.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/6/30.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/7/3.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/7/4.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/7/7.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/7/10.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/7/14.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/7/17.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/7/21.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/7/23.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/7/24.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/7/28.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/7/31.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/8/4.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/8/7.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/8/11.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/8/14.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/8/18.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/8/21.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/8/25.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/8/28.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/9/4.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/9/8.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/9/11.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/9/15.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/9/18.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/9/22.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/9/25.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/9/29.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/10/2.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/10/5.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/10/6.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/10/7.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/10/8.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/10/9.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/10/12.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/10/13.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/10/14.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/10/15.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/10/16.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/10/19.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/10/20.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/10/21.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/10/22.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/10/23.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/10/26.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/10/27.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/10/28.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/10/29.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/10/30.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/11/2.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/11/3.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/11/4.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/11/5.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/11/6.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/11/10.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/11/11.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/11/12.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/11/13.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/11/16.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/11/17.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/11/18.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/11/19.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/11/20.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/11/23.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/11/24.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/11/25.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/11/26.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/11/27.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/11/29.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/11/30.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/12/1.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/12/2.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/12/3.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/12/4.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/12/7.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/12/8.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/12/9.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/12/10.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/12/11.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/12/14.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/12/15.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/12/16.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/12/17.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/12/18.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/12/21.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/12/22.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/12/23.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/12/29.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/12/30.html",
        ]

        self.assertEquals(len(expected), len(result))
        for index, expected_url in enumerate(expected):
            result_url = result[index]
            self.assertEquals(expected_url, result_url)


class TestDayCrawling(unittest.TestCase):

    def setUp(self):
        # Given an archive page of the NY Times
        test_data_path = os.path.join(test_dir_path, 'data/themoscowtimes_day_sample.html')
        with open(test_data_path, 'r', encoding='cp1251') as f:
            self.html_data = f.read().replace('\n', '')
        # And a Crawler configured to extract article urls
        self.queries = [
            "//div[@class='content']/div[@class='left']//a/@href",
        ]

    def test_extraction(self):
        crawler = Crawler(
            self.queries,
            fetcher=MockFetcher(self.html_data)
        )

        # When the crawler extracts data from the archive page
        test_url = "http://old.themoscowtimes.com/sitemap/free/1992/5/8.html"
        result = crawler.crawl(test_url)

        # Then it will have queued the Orders
        expected = [
            "http://old.themoscowtimes.com/sitemap/free/1992/5/article/american-was-assassinated-family-says/221589.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/5/article/pepsi-to-save-vodka-cola-deal/221588.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/5/article/soviet-trucks-to-roll-westwards/221587.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/5/article/british-womens-club-formed/221586.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/5/article/yacht-club-launches-lessons-and-cruises/221585.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/5/article/top-yeltsin-advisor-asks-to-step-down/221584.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/5/article/birthday-magic/221583.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/5/article/russians-clash-with-u-s-on-nuclear-arms-control/221582.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/5/article/health-workers-strike-threatens-government/221581.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/5/article/vodka-price-hikes-unlikely-to-effect-drinking-habits/221580.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/5/article/firm-denies-finding-cpsu-billions/221579.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/5/article/secret-archives-just-a-peek/221578.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/5/article/tretyakov-promised-15-million/221577.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/5/article/victory-day-festivities/221576.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/5/article/communists-fights-back/221575.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/5/article/jack-the-ripper-sentenced-to-death/221574.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/5/article/corpses-crowd-city-morgues/221573.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/5/article/ex-spy-blake-calls-chocolate-cake-reports-rubbish/221572.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/5/article/asylum-seeking-north-korean-under-siege/221571.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/5/article/the-man-who-would-be-president/221570.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/5/article/teen-mafia-rules-moscow-streets/221569.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/5/article/opposition-forces-oust-tajik-president/221568.html",
            "http://old.themoscowtimes.com/sitemap/free/1992/5/article/august-1-convertible-ruble-a-long-shot-bet/221567.html",
        ]
        self.assertEquals(len(expected), len(result))
        for index, expected_url in enumerate(expected):
            result_url = result[index]
            self.assertEquals(expected_url, result_url)
