from peewee import *

db = SqliteDatabase('moradoresDB.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    nome = CharField()
    cpf = CharField(unique=True)
    bloco = IntegerField()
    apartamento = IntegerField()
    tipo = CharField()

class Vote(BaseModel):
    user = ForeignKeyField(User, backref='votes')
    voted_for = CharField()
    apartamento = IntegerField()
def initialize_db():
    db.connect()
    db.create_tables([User, Vote], safe=True)
    db.close() 