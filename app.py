from flask import Flask, render_template, url_for, request, jsonify
import requests
from db_logic import DBConnection
app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/registration.json')
def register():
	db = DBConnection()
	params = request.args
	if len(db.get('members', fname=params['fname'], lname=params['lname'])) == 0:
		db.insert('members', **params)
		return jsonify(already_inserted='false')
	else:
		return jsonify(already_inserted='true')

if __name__ == '__main__':
	app.run()