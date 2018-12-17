# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import dynamicIpTool

ip_pool = dynamicIpTool.IPPool()

alitrip_index = 'https://www.alitrip.com/'
google_test = 'https://www.google.com/'
proxy_option = webdriver.ChromeOptions()
proxy_ip = '181.221.18.35'
proxy_port = '63088'
proxy_ip_info =ip_pool.random_ip_address()
# proxy_option.add_argument('--proxy-server=socks5://'+proxy_ip+':'+proxy_port)
print("the proxy ip info is "+ proxy_ip_info)
proxy_option.add_argument('--proxy-server='+proxy_ip_info)
driver = webdriver.Chrome('F:\chrome webDriver\chromedriver_win32\chromedriver.exe',chrome_options=proxy_option)

driver.get(alitrip_index)
# driver.get(google_test)

alitrip_start_city = driver.find_element_by_name('depCityName')
alitrip_start_date = driver.find_element_by_name('depDate')
alitrip_arrive_city = driver.find_element_by_name('arrCityName')
alitrip_arrive_date = driver.find_element_by_name('arrDate')

alitrip_from = driver.find_element_by_id('J_FlightForm')
print(type("合肥"))
print(type(("合肥").decode('utf-8')))

alitrip_start_city.clear()
alitrip_start_city.send_keys("合肥".decode("utf-8"))
time.sleep(.05)
alitrip_arrive_city.clear()
alitrip_arrive_city.send_keys("上海".decode('utf-8'))
time.sleep(.05)
alitrip_start_date.clear()
alitrip_start_date.send_keys('2017-10-01')
# time.sleep(.2)
alitrip_arrive_city.send_keys(Keys.TAB)
alitrip_from.submit()
time.sleep(.2)
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[-1]) # switch to the new tab
time.sleep(0.1)
result_page_html = driver.page_source
result_page_soup = BeautifulSoup(result_page_html,'lxml')
all_results = result_page_soup.find('div',id='J_FlightListBox')
result_items = all_results.find_all('div', recursive=False)
print("found {0} records".format(len(result_items)))
for result_flight in result_items:
    print (result_flight.text)

# print(driver.page_source)