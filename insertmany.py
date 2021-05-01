from model import Anime
import peewee
import datetime
from animescrape import scrapeAnime
db=peewee.SqliteDatabase('anime.db')
'''
data=scrapeAnime()



with db.atomic():
    query=Anime.insert_many(data)
    query.execute()'''

'''
#aggregate functions:
contains
startswith
offset
limit
endswith
'''
#.where(Anime.title.startswith('R'))
#x=int(input('Enter ID number to delete: '))
#delete=Anime.delete_by_id(x)
delete=Anime.delete().where(Anime.id<10)
delete.execute()

anime=Anime.select().order_by(Anime.title.desc())
for a in anime:
    print(a.id,a.title,a.videos)
