import peewee
import datetime

db=peewee.SqliteDatabase('anime.db')
class Anime(peewee.Model):
    title=peewee.TextField()
    videos=peewee.CharField()


    class Meta:
        database=db
        table_name='tblgames'
Anime.create_table()
