from pymongo import Connection

class DBConnection(object):
	def __init__(self):
		self.db = Connection('localhost', 27017).curc

	def insert(self, c, **kw):
		self.db[c].insert(kw)

	def get(self, c, **kw):
		return list(self.db[c].find(kw))

	def update(self, c, match, **kw):
		self.db[c].update(match, {'$set' : kw})