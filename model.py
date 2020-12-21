from peewee import SqliteDatabase, Model, CharField, SmallIntegerField, ForeignKeyField

database = SqliteDatabase('chart.db')


class BaseModel(Model):
    class Meta:
        database = database


class Song(BaseModel):
    position = SmallIntegerField()
    name = CharField()

    class Meta:
        table_name = 'songs'


class Author(BaseModel):
    name = CharField()

    class Meta:
        table_name = 'authors'


class Performance(BaseModel):
    song = ForeignKeyField(Song, to_field='id')
    author = ForeignKeyField(Author, to_field='id')

    class Meta:
        table_name = 'performances'


database.connect()
database.drop_tables([Song, Author, Performance])
database.create_tables([Song, Author, Performance])
database.close()
