import datetime
from flask import Flask, render_template, url_for, request, jsonify
from werkzeug.contrib.fixers import ProxyFix
import requests
from db_logic import DBConnection
app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
	db = DBConnection()
	num_members = db.get('members',gym='mphc')
	if len(num_members) >= 50:
		return render_template('index.html', mphc_available=False)
	return render_template('index.html', mphc_available=True)

@app.route('/registration.json')
def register():
	db = DBConnection()
	d = request.args
	params = {k:v for k,v in d.iteritems()}
	params['gender'] = params.pop('gensel')
	params['driver'] = True if params.pop('dsel') is 'y' else False
	params['graduating'] = True if params.pop('gsel') is 'y' else False
	params['shirt'] = params.pop('ssel')
	params['gym'] = params.pop('msel')
	if len(db.get('members', fname=params['fname'], lname=params['lname'])) == 0:
		db.insert('members',timestamp=datetime.datetime.utcnow(),**params)
		return jsonify(already_inserted='false')
	else:
		return jsonify(already_inserted='true')

app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == '__main__':
	app.run()
