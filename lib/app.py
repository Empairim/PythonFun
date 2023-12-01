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
#seeding database tables


app = Flask(__name__)
# dunder name and creating Flask application


@app.route('/')
def index():
    return "Hello World"
# testing to see if server is running before I start

@app.route('/person/' methods=['GET', 'POST'])
@app.route('/person/' methods=['GET', 'PUT', "DELETE"])
#setting up routes and slugs also what  HTTP VERB each route has access to
def endpoint(id=None):#set id to none by defualt so that the first router isnt stuck looking for it
    if request.method == 'GET':
        if id:# if the get request has an id obvoiusly do the below
            return jsonify(model_to_dict(Person.get(Person.id == id))) #basically if person has an id return that data in a json format and searching the person dict for the id key
    else: #if no id for get give me an empty list/array and fill it with the information from the person table
        people_list = []
        for people in Person.select():
            people_list.append(model_to_dict(people))
        return jsonify(people_list)#select is from peewee its like if we did SELECT * FROM person but with the orm rather than the sql file or cli tool with a for loop obviously then return that array of json data
    if request.method == 'PUT':
        body = request.get_json()# It is used to extract JSON data from the request body in Flask. and we're naming it body because it makes sense to
        Person.update(body).where(Person.id == id).execute()
        return "Person" + str(id) + "has been updated"
    if request.method == 'POST':
        new_person = dict_to_model(Person, request.get_json())
        new_person.save()
        return jsonify({"Success: True"})
    if request.method == 'DELETE':
        Person.delete().where(Person.id == id).execute()
        return "Person " + str(id) + " deleted."


app.run(debug=True)
#must always be last line
