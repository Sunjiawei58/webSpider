# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

import urllib2

import sys
reload(sys)
sys.setdefaultencoding('UTF8')
import time

filename = 'result.txt'

sys.stdout = open(filename,'w')

def main():
    maxPage = 200
    currentPage = 1
    while(currentPage<=maxPage):

        if(currentPage == 1):

            sauce = urllib2.urlopen('http://www.chinacaipu.com/menu/chinacaipu/').read()
            soup = BeautifulSoup(sauce,"lxml")
            # print(soup.prettify())
            # print(soup.body.prettify())

            for subdiv in soup.find_all('div'):
                if(subdiv.get('class')!=None and subdiv.get('class')[0] == 'c_con3'):
                    for food in subdiv.ul.find_all('li'):
                        print(food.img.get("alt").encode('utf-8'))

                    # print(title.ul.li.img.get('alt'))
            currentPage+=1
            continue
        sauce = urllib2.urlopen('http://www.chinacaipu.com/menu/chinacaipu/index_'+str(currentPage)+".html").read()
        soup = BeautifulSoup(sauce, "lxml")
        for subdiv in soup.find_all('div'):
            if (subdiv.get('class') != None and subdiv.get('class')[0] == 'c_con3'):
                for food in subdiv.ul.find_all('li'):
                    foodName = food.img.get('alt')
                    if(foodName.find('的做法') != -1):
                        suffexIndex = foodName.index('的做法')
                        print(foodName[0:suffexIndex].encode('utf-8'))
                    else:
                        print(food.img.get("alt").encode('utf-8'))


        currentPage += 1
        time.sleep(0.5)
main()

