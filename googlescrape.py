from bs4 import BeautifulSoup
import requests

website="https://www.google.com"
r=requests.get(website)
data=r.text

soup=BeautifulSoup(data, 'html.parser')
#print(soup.prettify())

#print(soup.p)
#print(soup.find('a'))
#print(soup.find(id=SIvCob))
google=soup.find(id='SIvCob')
print(google.get_text())
a,b,c,d,e = google.get_text().split()
print(a)
print(b)
print(c)
print(d)
print(e)



'''for link in soup.find_all("a"):
    print(link.get("href"))'''
