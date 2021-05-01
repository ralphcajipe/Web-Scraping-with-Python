from bs4 import BeautifulSoup
import requests
from datetime import datetime


url = "https://en.wikipedia.org/wiki/Computer"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'html.parser')

list1=[]
list2=[]
level1=soup.find_all('li',{'class':'toclevel-1'})
level2=soup.find_all('li',{'class':'toclevel-2'})
for x in level1:
    t = x.find('span',{'class':'tocnumber'})
    v = x.find('span',{'class':'toctext'})
    list1.append([t.get_text().strip(),v.get_text().strip()])

for x in level2:
    t = x.find('span',{'class':'tocnumber'})
    v = x.find('span',{'class':'toctext'})
    list1.append([t.get_text().strip(),v.get_text().strip()])


for x in range(len(list1)):
    print(list[x])
