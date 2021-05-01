from bs4 import BeautifulSoup
import requests
from datetime import datetime

def scrapeAnime():
    url = "https://www.crunchyroll.com/videos/anime"
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    now = datetime.now()
    listAnime=[]
    anime=soup.find_all('li',{'class':'hover-bubble group-item'})
    for x in anime:
        t = x.find('span',{'class':'series-title'})
        v = x.find('span',{'class':'series-data'})
        #print(v.get_text().strip())
        #print(t.get_text().strip())
        listAnime.append([t.get_text().strip(),v.get_text().strip()])
    #print(listAnime)

    '''for list in range(len(listAnime)):
        print('{:<10d}{:<30s}{:<20s}{}'.format(list+1,listAnime[list][0],listAnime[list][1],now))
    '''

    data= [{'title':title,'videos':videos} for title, videos in listAnime]
    return(data)
