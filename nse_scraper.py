# import library
from bs4 import BeautifulSoup
import requests
import pandas as pd
# Request to website and download HTML contents
url='https://afx.kwayisi.org/nse/'
req=requests.get(url)
content=req.text
soup=BeautifulSoup(content, 'lxml')

required_data = soup.find(class_='t').find_all('tbody')
finalised_data = []
# print(required_data)
for data in required_data:
	row = data.find_all('td')
	for i in row:
		formatted=i.get_text(strip=True)
		finalised_data.append(formatted)
	

print(finalised_data)





