from flask import Flask, redirect, url_for, session, request, jsonify, Markup, make_response, render_template
from flask_oauthlib.client import OAuth
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
oauth = OAuth(app)

google = oauth.remote_app(
    'google',
    consumer_key=os.environ['GOOGLE_CLIENT_ID'],
    consumer_secret=os.environ['GOOGLE_CLIENT_SECRET'],
    request_token_params={
        'scope': 'email'
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)

client = pymongo.MongoClient(url)
db = client[os.environ["MONGO_DBNAME"]] 
collection = db['documents'] #put the name of your collection in the quotes
fs = gridfs.GridFS(db)

app.secret_key = os.environ['SECRET_KEY']
oauth = OAuth(app)

@app.route("/document-create", methods=['POST']) #create documentation post
def createDoc():
	lang = request.form['lang'] #create variable based on data from the language form
	text = str(request.form['doc']) #creates variable based on data from text/document form
	documents = db.documents
	collection.insert_one({'lang':1})

	poststr='<table> <tr> <th> Language:  </th> <th> Text: </th> </tr>' #creates Table with data
	poststr+='<td> ' + str(lang) + '</td> <br> <td>' + str(text) + '</td> </table>' #finishes table with values
	post += Markup(poststr)
	if post = '<table> <tr> <th> Language: </th> <th> Text: </th> </tr> <t
	r><td> ' + str(lang) + '</td> <br> <td>' + str(text) + '</td> </table>':
		print('everything should be working lmao')
	else:
		print("o shit it aint working OOF DAMN.")
		return post

@app.route('/')
def render_home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True, port="5000")
