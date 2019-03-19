#!/usr/bin/env python
# coding: utf-8

# In[2]:





# In[ ]:





# In[5]:





# In[6]:





# In[7]:





# In[8]:





# In[9]:





# In[10]:





# In[11]:





# In[12]:





# In[14]:





# In[15]:





# In[16]:





# In[17]:





# In[18]:





# In[19]:





# In[20]:





# In[21]:





# In[22]:





# In[74]:





# In[170]:


import pandas as pd
import requests
import seaborn as sns
import urllib.request
import numpy as np
from urllib.request import urlopen
import matplotlib.pyplot as plt
import csv
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
type(soup)
#from time import sleep

pages = []
i = []

for i in range(1, 48):
    
    #Diplomky
    #url = 'https://dspace.cuni.cz/handle/20.500.11956/1905/discover?rpp=10&page=' + str(i) + '&group_by=none&etal=0&filtertype_0=ds_workType&filtertype_1=ds_facultyDepartment&filter_0=diplomov%C3%A1+pr%C3%A1ce&filter_relational_operator_1=equals&filter_1=Katedra+sociologie&filter_relational_operator_0=equals'
    
    #Bakalářské práce
    #url = 'https://dspace.cuni.cz/handle/20.500.11956/1905/discover?rpp=10&page=' + str(i) + '&group_by=none&etal=0&filtertype_0=ds_facultyDepartment&filtertype_1=ds_workType&filter_0=Katedra+sociologie&filter_relational_operator_1=equals&filter_1=bakal%C3%A1%C5%99sk%C3%A1+pr%C3%A1ce&filter_relational_operator_0=equals'
    
    #Disertace
    url = 'https://dspace.cuni.cz/handle/20.500.11956/1905/discover?rpp=10&page=' + str(i) + '&group_by=none&etal=0&filtertype_0=ds_workType&filtertype_1=ds_facultyDepartment&filter_0=dizerta%C4%8Dn%C3%AD+pr%C3%A1ce&filter_relational_operator_1=equals&filter_1=Katedra+sociologie&filter_relational_operator_0=equals'
    pages.append(url)
    i = i+1
    #sleep(5)
  
    for page in pages:
        r = requests.get(page)
        soup = BeautifulSoup(r.text, 'html.parser')
    
        titles = soup.find_all('h4')

        if i == 48:    
            for title in titles:
                print(title.get_text())
                  


# In[ ]:





# In[ ]:





# In[ ]:




