from bs4 import BeautifulSoup
import requests
from datetime import datetime

url = "https://en.wikipedia.org/wiki/Computer"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'html.parser')
#list1=[]
#list2=[]

level1 = soup.find_all('span',{'class':'tocnumber'})
level2 = soup.find_all('span',{'class':'toctext'})

for x in range(len(level1)):
    print()
    print(level1[x].get_text().strip(),level2[x].get_text().strip())
