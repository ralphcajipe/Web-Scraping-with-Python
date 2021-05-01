from bs4 import BeautifulSoup
import requests
from datetime import datetime

url = "https://weather.com/en-IN/weather/today/l/1714bf7d7bb450067a85ed7c3231952950a3861029e517e66d2434c9a591ded3"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'html.parser')


#tr = soup.find('div',{'class':"today_nowcard-sidecar component panel"})
place = soup.find('h1',{'class':"h4 today_nowcard-location"})
time = soup.find('p',{'class':"today_nowcard-timestamp"})
condition = soup.find('span',{'class':"today-wx-descrip"})
temp = soup.find('div',{'class':"today_nowcard-temp"})
#humid = soup.find('li',{'class':"wx-detail"})
wind = soup.find('li',{'class':"wx-detail"})

wind=int(wind)

if wind >=50km/h:
    print:('Stay in your house!')
else:
    print('Enjoy your day!')'''

print(place.get_text().strip())
print(time.get_text().strip())
print(condition.get_text().strip())
print(temp.get_text().strip())
print(humid.get_text().strip())
print(wind.get_text().strip())




#for x in range(len(place)):
    #print(place.get_text().strip())
