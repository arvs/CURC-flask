from flask import Flask, render_template, url_for, request, jsonify
import requests
from db_logic import DBConnection
app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/search_for_prof')
def search_for_prof():
	db = DBConnection()
	name = request.args.get("name","")
	db.insert('classes', Instructor = name, link=x)
	return jsonify(name=name, classes=[])

if __name__ == '__main__':
	app.run()