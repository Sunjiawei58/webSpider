# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import urllib
import mechanize


br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.2;\
                    WOW64) AppleWebKit/537.11 (KHTML, like Gecko)\
                    Chrome/23.0.1271.97 Safari/537.11')]
term = '常见问题'
keywords = urllib.quote_plus(term)
print("keywords is "+keywords)
query = "https://www.google.com/search?q="+keywords+"&oq="+keywords

htmltext = br.open(query).read()
soup = BeautifulSoup(htmltext,"lxml")
all_links =  soup.find_all('h3',{'class':'r'})   # resource link

for header in all_links:
    link = header.a["href"]
    print(header.a)

    # link_html = br.open(link).read();
    # sub_soup = BeautifulSoup(link_html, 'lxml')
    # for sub_link in sub_soup.find_all('a'):
    #     # print(link.string)
    #     if(sub_link.string!=None):
    #         if (sub_link.string.encode("utf-8") == "常见问题"):
    #             print("found the faq page!!!"+link+sub_link["href"][1:])
    # link_html = br.open(links["href"]).read()
    # sub_soup = BeautifulSoup(link_html,'lxml')
    # for link in sub_soup.find_all('a'):
    #     # print(link.string)
    #     if(link.string!=None):
    #         if (link.string.encode("utf-8") == "常见问题"):
    #             print("found the faq page!!!"+link["href"])
    # print(links)
nextpage = soup.find("a",{"id":"pnnext"})
print(nextpage["href"])
nextpage_query = "https://www.google.com"+nextpage["href"]
print(nextpage_query)
# print (nextpage[0].href)
# print (soup.find_all('a'))