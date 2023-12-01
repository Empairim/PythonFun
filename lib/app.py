from flask import Flask, request, jsonify
# importing basic stuff for server


app = Flask(__name__)
# dunder name and creating Flask application


@app.route('/')
def index():
    return "Hello World"
# testing to see if server is running before I start


app.run(debug=True)
