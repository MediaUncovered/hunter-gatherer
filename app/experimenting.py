# import requests
# from bs4 import BeautifulSoup
#
# req = requests.get("https://query.nytimes.com/search/sitesearch/#/*/since1851/document_type%3A%22article%22/1/allauthors/oldest/")
# soup = BeautifulSoup(req.text, 'html.parser')
# for link in doc.xpath("//li[contains(concat(' ', @class, ' '), ' story ')]/div/h3/a"):
#     print(link)

# TODO start phantomjs before running this script
from selenium import webdriver

driver = webdriver.PhantomJS()
driver.implicitly_wait(10)
driver.get("https://query.nytimes.com/search/sitesearch/#/*/since1851/document_type%3A%22article%22/1/allauthors/oldest/")
driver.find_element_by_css_selector("#searchResults li.story")
print("found the stories")
