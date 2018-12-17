# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

import urllib2

import sys
reload(sys)
sys.setdefaultencoding('UTF8')
import time




class AirportCode():
    max_page=0
    current_page = 0

    def __init__(self):
        self.max_page = 40
        self.current_page = 1


    def get_airport_code(self):

        filename = 'airportCode.txt'
        sys.stdout = open(filename, 'w')
        # print('max_page is '+str(self.max_page))
        while self.current_page <= self.max_page:
            sauce = urllib2.urlopen('http://www.zou114.com/sanzidaima/index.asp?zm=&page='+str(self.current_page)).read()
            soup = BeautifulSoup(sauce, "lxml")

            table = soup.find('table')
            # print (table)
            for tr in table.find_all('tr'):
                # print("find one tr")
                # print(tr.get('onmouseout'))
                if(tr.get('onmouseout') == "this.bgColor='#FFFFFF'"):
                    code_list = tr.find_all('td')
                    print code_list[0].string + '\t' + code_list[1].string

                    # for text in tr.find_all('td')[:2]:
                    #     print text.string
            self.current_page+=1
    def get_wiki_chinese_airport_code(self):
        print 'enter wiki function'
        filename = 'wikiAirportCode.txt'
        sys.stdout = open(filename, 'w')

        sauce=urllib2.urlopen("https://zh.wikipedia.org/wiki/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E6%9C%BA%E5%9C%BA%E5%88%97%E8%A1%A8").read()
        soup = BeautifulSoup(sauce,"lxml")
        table = soup.find_all("table",style='font-size:small; text-align:center;')

        for t in table:
            # print t
            for table_content in t.find_all('tr'):
                if table_content.td:
                    td_content = table_content.find_all('td')
                    if td_content[3].string:
                        print td_content[3].string + '\t' + td_content[0].string


        # print len(table)

if __name__ == '__main__':
    airport = AirportCode()
    # airport.get_airport_code()
    airport.get_wiki_chinese_airport_code()