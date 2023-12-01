# dont for get dependencies pipenv install peewee flask psycopg2-binary


from flask import Flask, request, jsonify
# importing basic stuff for server
from peewee import *  # IMPORT ALL FROM peewee

# PLAYHOUSE FROM PEEWEE AND MODEL TO DICT IS PRETTY MUCH SAYING TRANSLATE ANY MODELS TO OBJECTS OR DICTIONARIES(PYTHON)
from playhouse.shortcuts import model_to_dict, dict_to_model
from datetime import date
db = PostgresqlData('people', user='poowoo',
                    password='123456', host='localhost', port=5432)
# connectiing to my postgress db named ppl with this information and port is Postgres defualt port I believe.


class BaseModel(Model):
    class Meta:
        database = db
# set ups my basemodel to be based on my database and its tables


class Person(BaseModel):
    name = CharField()
    birthday = DateField()
    age = IntegerField()
# setting up a person model/class based on whats in the basemodel class which references to the dbs models which is whats in its tables


db.connect()
db.drop_table([Person])
db.create_tables([Person])
# obvious connecting to db getting rid of old data and adding new

Person(name='Raul', birthday=date(1990, 1, 1), age=1000).save()
Person(name='Chris', birthday=date(1985, 5, 10), age=1000).save()
Person(name='Mega Hawk', birthday=date(1980, 12, 25), age=9999).save()


app = Flask(__name__)
# dunder name and creating Flask application


@app.route('/')
def index():
    return "Hello World"
# testing to see if server is running before I start


app.run(debug=True)
