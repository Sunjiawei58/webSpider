# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import urllib
import mechanize
import sys

page_number = 1
city_name = 'aomen'
max_number = 9
for page in range(1,max_number+1):
    sys.stdout = open(city_name+str(page)+'.txt', 'w')
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.2;\
                        WOW64) AppleWebKit/537.11 (KHTML, like Gecko)\
                        Chrome/23.0.1271.97 Safari/537.11')]
    query = "https://"+city_name+".8684.cn/line"+str(page)
    query_base = "https://"+city_name+".8684.cn"
    wrong_website_list = []
    current_website = ''
    try:

        htmltext = br.open(query).read()
        soup = BeautifulSoup(htmltext, "lxml")
        # all_links =  soup.find_all('h3',{'class':'r'})   # resource link
        all_bus_div = soup.find_all('div', {"id": "con_site_1"})

        for header in all_bus_div[0].children:
            link_text = header.text
            link_adress = header['href']
            print(link_text).encode('utf-8')
            new_address = query_base + link_adress
            current_website = new_address
            detailed_html = br.open(new_address).read()
            detailed_soup = BeautifulSoup(detailed_html, "lxml")
            all_detailed_div_list = detailed_soup.find_all('div', {"class": "bus_line_site"})
            print(len(all_detailed_div_list))
            for trip in all_detailed_div_list:
                for station_div_list in trip.children:
                    for station_div in station_div_list.children:
                        station_text = station_div.a.text
                        print(station_text).encode('utf-8')
                print('-----返程-----')
    except Exception, e:
        wrong_website_list.append(current_website)
        print('there is something wrong with the internet')
