#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver

driver = webdriver.PhantomJS()
driver.implicitly_wait(10)
driver.get("https://query.nytimes.com/search/sitesearch/#/*/from19810101to20171231/document_type%3A%22article%22/1/allauthors/oldest/")
driver.find_element_by_css_selector("#searchResults li.story")

print("found stories\n\n")
driver.page_source
with open("ny_archive_sample.html", "w") as f:
    f.write(driver.page_source.encode("UTF-8"))
print("written to file")
