
from bs4.builder import ParserRejectedMarkup
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
print('========.=========.=======')
print('invoirment setup is done')
data=[['Name_candidate','Party']]
n=10
for i in range(n):
    url='https://prsindia.org/mlatrack?state=Uttar+Pradesh&assembly_term=17&name=&education=&constituency=&party=&gender=All'
    r=requests.get(url)
    html_content=r.content
    soup=BeautifulSoup(html_content, 'html.parser')
    page=soup.find_all(attrs={'class':"views-field views-field-title-field"})
    part_n=soup.find_all(attrs={'class':"views-field views-field-field-political-party"})

    Name_candidate=page[i].text.replace('\n'," ")
    Party=part_n[i].text.replace('\n'," ")
    data.insert(i,[Name_candidate,Party])
    print(i)


df=pd.DataFrame(data,columns=['Candidate_Name','Party'])
df.to_csv('UP_MLA.csv')
