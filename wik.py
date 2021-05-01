from bs4 import BeautifulSoup
import requests


url = "https://en.wikipedia.org/wiki/Computer"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'html.parser')

wiki1=soup.find_all('li',{'class':'toclevel-1'})

w=0
for x in wiki1:
    w=w+1
    print(x.get_text())
