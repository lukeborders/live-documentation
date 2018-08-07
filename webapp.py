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
app.debug = False

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

@app.route('/')
def render_home():
   	   session['user'] = 'Luke'
   	   return render_template('home.html')

@app.route("/document-create", methods=['POST']) #create documentation post
def createDoc():
	global lang = request.form['lang'] #create variable based on data from the language form
	global text = request.args['doc']  #creates variable based on data from text/document form
	db.collection.insert({ 'text': doc })
	db.collection.insert({ 'lang': lang }) 
	return render_template('/document-create')

def showPost():
	tbl='<table> <tr> <td> Language </td> <td> Text </td> </tr>'
	for document in db.collection.find():
		if session['user']:
			tbl += "<tr>"
			tbl += "<td>"
			tbl += str(doc['lang'])
			tbl += "</td>"
			tbl += "<td>"
			tbl += str(doc['text'])
			tbl += "</td>"
			tbl += "</tr>"
			tbl += "</table>"
			return Markup(tbl)
		
if __name__ == '__main__':
    app.run(debug=True, port="5000")
