# -*- coding: utf-8 -*-
import sys
from selenium import webdriver

sys.stdout = open('AreaResultBJ.txt','w')
mei_tuan_site = 'http://bj.meituan.com/meishi/'
proxy_option = webdriver.ChromeOptions()
driver = webdriver.Chrome('F:\chrome webDriver\chromedriver_win32\chromedriver.exe',chrome_options=proxy_option)
driver.get(mei_tuan_site)

js_script = 'return window._appState.filters.areas'
areas = driver.execute_script(js_script)

for area in areas:
    # print area[u'name'].encode('utf-8'),
    # print ':\t'
    for x in range(1,len(area[u'subAreas'])):
        print (area[u'subAreas'][x][u'name'].encode('utf-8') + ' ')

