# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

ctrip_mobile_index = 'http://m.ctrip.com/html5/Flight/swift/index'

driver = webdriver.Chrome('F:\chrome webDriver\chromedriver_win32\chromedriver.exe')

driver.get(ctrip_mobile_index)

