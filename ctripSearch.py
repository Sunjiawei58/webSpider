# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import mechanize
import urllib2
import time
#needs to import selenium for scraping the javasript
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



# br = mechanize.Browser()
# br.set_handle_robots(False)
# br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.2;\
#                     WOW64) AppleWebKit/537.11 (KHTML, like Gecko)\
#                     Chrome/23.0.1271.97 Safari/537.11')]
query = "http://flights.ctrip.com/booking/sha-bjs-day-1.html?ddate1=2017-10-04/"
ctrip_index = 'http://flights.ctrip.com/domestic/'
# ctrip_html = br.open(query)


driver = webdriver.Chrome('F:\chrome webDriver\chromedriver_win32\chromedriver.exe')
# driver.get(query)
# time.sleep(2)    # this is for getting flight result
driver.get(ctrip_index)
# time.sleep(3)
ctrip_start_city = driver.find_element_by_id('DepartCity1TextBox')
ctrip_start_date = driver.find_element_by_id('DepartDate1TextBox')
ctrip_destinate_city = driver.find_element_by_id('ArriveCity1TextBox')
ctrip_search_button = driver.find_element_by_id('search_btn')
ctrip_search_form = driver.find_element_by_id('J_filghtSearch')
# ctrip_start_city = driver.find_element_by_css_selector('#FD_StartCity')
# ctrip_start_city = driver.find_element_by_xpath("//div[@id='searchBox']/div[2]/form[1]/div[4]/input[@id='FD_StartCity']")
print(ctrip_start_city.is_displayed())
# ctrip_start_city.clear()
ctrip_start_city.send_keys('SHA',Keys.TAB) # needs to get the auto fill thing
time.sleep(.2)

ctrip_destinate_city.send_keys('BJS')
time.sleep(.2)
ctrip_start_city.send_keys(Keys.TAB)
ctrip_start_date.send_keys('2017-10-01')
time.sleep(.2)
ctrip_start_city.send_keys(Keys.TAB)

ctrip_search_form.submit()


ctrip_htmltext = driver.page_source
# print(ctrip_htmltext)

# time.sleep(2)   # sleep 2 second for waiting ajax result
# ctrip_htmltext = ctrip_html.read()
# ctrip_htmltext = urllib2.urlopen("http://flights.ctrip.com/booking/sha-bjs-day-1.html?ddate1=2017-10-04/").read()
soup = BeautifulSoup(ctrip_htmltext,'lxml')
# print(soup)


# flight_info_list  = soup.find_all('div', class_='search_box search_box_tag search_box_light ')
# for flight_info in flight_info_list:
#     flight_num = flight_info.find('td',class_='logo').text
#     print(flight_num)
#     flight_dep_airport = flight_info.find('td',class_='right').text.encode('utf-8').lstrip(' ')
#     flight_arr_airport = flight_info.find('td',class_='left').text.encode('utf-8').lstrip(' ')
#     flight_time_effiency = flight_info.find('td',class_='service').text.encode('utf-8').lstrip(' ')
#     flight_price = flight_info.find('td',class_='price').text.encode('utf-8').lstrip(' ')
#
#     print(flight_dep_airport)
#     print(flight_arr_airport)
#     print(flight_time_effiency)
#     print(flight_price)
#
# print(len(flight_info_list))
#
# driver.close()
