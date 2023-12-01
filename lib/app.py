#dont for get dependencies pipenv install peewee flask psycopg2-binary


from flask import Flask, request, jsonify
# importing basic stuff for server
from peewee import #IMPORT ALL FROM peewee

from playhouse.shortcuts import model_to_dict, dict_to_model # PLAYHOUSE FROM PEEWEE AND MODEL TO DICT IS PRETTY MUCH SAYING TRANSLATE ANY MODELS TO OBJECTS OR DICTIONARIES(PYTHON)


app = Flask(__name__)
# dunder name and creating Flask application


@app.route('/')
def index():
    return "Hello World"
# testing to see if server is running before I start


app.run(debug=True)
