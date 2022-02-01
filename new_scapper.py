from bs4.builder import ParserRejectedMarkup
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
print('========.=========.=======')
print('invoirment setup is done')
url='https://codewithharry.com'
#html content
#html parser
#html beautiful soup
r=requests.get(url)
#print(r.content)
html_content=r.content
soup=BeautifulSoup(html_content, 'html.parser')
#use prittify
title=soup.title
print(title)
print(type(title))
paras=soup.find_all('p')

"""
this is a  pyhton scipt for scrape  the data from any  site for that is bassoically  is  not encrepeted
means that is not cloud based encripted 


"""
anchers=soup.find_all('a')
#print(ancher)
#print(soup.find('p')['class'])
#print(soup.find_all('p' ,class_='lead'))

#get text from the gs /soup
print('========.========.=======')
#print(soup.get_text())
all_links=set()
for link in anchers:
    if (link!='#'):
        link='http://codewithharry'+link.get('href')
        all_links.add(link)


for val in all_links:
    print(val ,end=' \n ')
