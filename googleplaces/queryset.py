# Google Places for Python
# Adrien Katsuya Tateno 2014

from datetime import datetime

class Queryset:
	_data = []
	_timestamp = None

	def __init__(self, data=None):
		self._timestamp = datetime.now()
		if data:
			self._data = data

	def data(self):
		return self._data

	def names(self):
		lst = []
		for datum in self._data:
			lst.append(datum[u'name'])
		return lst

	def filter(self, fn):
		lst = []
		for datum in self._data:
			if fn(datum):
				lst.append(datum)
		return Queryset(lst)

	def __add__(self, other):
		return Queryset(self._data + other._data)
	def __iadd__(self, other):
		self._data += other._data

	def __nonzero__(self):
		if _timestamp:
			return True
		else:
			return False

	def __getitem__(self, i):
		return self._data[i]
	def __setitem__(self, i, value):
		self._data[i] = value