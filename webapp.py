from flask import Flask, redirect, url_for, session, request, jsonify, Markup, make_response, render_template
from flask_pymongo import PyMongo
from bson import ObjectId
from flask import flash
from threading import Lock
from pymongo import MongoClient



import pprint
import os
import json
import pymongo
import gridfs
import sys

app = Flask(__name__)

url = 'mongodb://{}:{}@{}:{}/{}'.format(
        os.environ["MONGO_USERNAME"],
        os.environ["MONGO_PASSWORD"],
        os.environ["MONGO_HOST"],
        os.environ["MONGO_PORT"],
        os.environ["MONGO_DBNAME"])

app.secret_key = os.environ['SECRET_KEY']

client = pymongo.MongoClient(url)
db = client[os.environ["MONGO_DBNAME"]]
collection = db['documents'] #put the name of your collection in the quotes
fs = gridfs.GridFS(db)

app.secret_key = os.environ['SECRET_KEY']
oauth = OAuth(app)


@app.route('/')
def render_home():
   	   session['user'] = 'Luke'
   	   return render_template('home.html')

@app.route("/document-create", methods=['POST']) #create documentation post
def createDoc():
	lang = request.form['lang'] #create variable based on data from the language form
	text = request.form['doc']  #creates variable based on data from text/document form
	db.collection.insert_one({'lang':lang}) # create document with 'lang ' as its key and the language variable as its value 
	Markup +='<h1> Language: ' + str(lang) + '</h1>' + '<br>' + '<h1> Text: ' + str(text) + '</h1>'
   return Markup

if __name__ == '__main__':
    app.run(debug=True, port="5000")
