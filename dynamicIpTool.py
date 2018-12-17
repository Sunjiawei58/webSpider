# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

import urllib2
import mechanize
from random import randint


class IPPool:

    def __init__(self):
        self.ips=[]
        self.br = mechanize.Browser()
        self.br.set_handle_robots(False)
        self.br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.2;\
                            WOW64) AppleWebKit/537.11 (KHTML, like Gecko)\
                            Chrome/23.0.1271.97 Safari/537.11')]
        self.add_ip_into_pool()
    def add_ip_into_pool(self):

        ip_pool_index = 'https://www.socks-proxy.net/'

        ip_pool_html = self.br.open(ip_pool_index).read()

        soup = BeautifulSoup(ip_pool_html,'lxml')

        result_table = soup.find('table',id='proxylisttable')

        tr_list = result_table.tbody.find_all('tr')
        for element in tr_list:
            ip_datas = element.find_all('td')
            if ip_datas[4].get_text() == 'Socks5':
                ip_address = '{0}://{1}:{2}'.format(ip_datas[4].get_text(),ip_datas[0].get_text(),ip_datas[1].get_text())
            # ip_address = ip_datas[4].get_text() + '://'+ ip_datas[0].get_text() + ':' + ip_datas[1].get_text
                print(ip_address)
                self.ips.append(ip_address)
            else:
                continue
    def random_ip_address(self):
        ip_index = randint(0,len(self.ips)-1)
        return self.ips[ip_index]

ip_pool = IPPool()
ip_pool.add_ip_into_pool()