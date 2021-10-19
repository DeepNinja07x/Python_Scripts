#!/usr/bin/env python

#Requirements
  #requests
  #bs4


from bs4 import BeautifulSoup
import requests
from selenium import webdriver


url= raw_input("enter url: ")
source=requests.get(url)


def get_chrome_web_driver(options):
    return webdriver.Chrome("./chromedriver", chrome_options=options)


def get_web_driver_options():
    return webdriver.ChromeOptions()


def set_ignore_certificate_error(options):
    options.add_argument('--ignore-certificate-errors')


def set_browser_as_incognito(options):
    options.add_argument('--incognito')

soup=BeautifulSoup(source.text,'html')

title=soup.find('title')
print("this is with html tags :",title)

qwery=soup.find('h1')
print("this is without html tags:",qwery.text) 


links=soup.find('a')
print(links)
print(links['href']) 
print(links['class'])

many_link=soup.find_all('a')
total_links=len(many_link)
print("total links in my website :",total_links)
print()
for i in many_link[:6]:
    print(i)

second_link=many_link[1]
print(second_link)
print()
print("href is :",second_link['href'])

nested_div=second_link.find('div')
print(nested_div)
print()
z=(nested_div['class'])
print(z)
print(type(z))
print()
print("class name of div is :"," ".join(nested_div['class'])) 

wiki=requests.get("https://en.wikipedia.org/wiki/World_War_II")
soup=BeautifulSoup(wiki.text,'html')
print(soup.find('title'))

ww2_contents=soup.find_all("div",class_='toc')
for i in ww2_contents:
    print(i.text)

overview=soup.find_all('table',class_='infobox vevent')
for z in overview:
    print(z.text)