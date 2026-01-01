#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup
import csv


# In[3]:


url = "https://www.worldometers.info/co2-emissions/"


# In[4]:


response = requests.get(url)
if response.status_code != 200:
    raise Exception(f"Failed to fetch page: {response.status_code}")


# In[7]:


response


# In[5]:


soup = BeautifulSoup(response.text, "html.parser")


# In[6]:


table = soup.find("table")


# In[ ]:


if table is None:
    raise Exception("Could not find the emissions table on the page")


# In[8]:


headers = []
for th in table.find_all("th"):
    headers.append(th.text.strip())


# In[9]:


rows = []
for tr in table.find_all("tr")[1:]:  # skip header row
    cells = tr.find_all(["td", "th"])
    if len(cells) == 0:
        continue
    row = [cell.text.strip() for cell in cells]
    rows.append(row)


# In[10]:


with open("co2_emissions_by_country.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)


# In[11]:


print("Scraping completed. Data saved to co2_emissions_by_country.csv")


# In[ ]:




