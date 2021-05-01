from model import Game
import datetime

ig=input('IGN: ')
gen=input('GENRE: ')
developer=input('DEVELOPER: ')
rd=int(input('RELEASED DATE:'))
y,m,d=rd.split()

Game.create(ign=ig,genre=gen,
dev=developer,releasedate=datetime.datetime(int(y),int(m),int(d)))#Year,Month,Day
g=Game.select()
for games in g:
    print(games.ign,games.genre,games.dev,games.releasedate)
