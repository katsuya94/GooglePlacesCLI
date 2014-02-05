# Google Places for Python
# Adrien Katsuya Tateno 2014

from urllib2 import urlopen
from json import loads
from datetime import datetime, timedelta
from queryset import Queryset

class PlacesError(StandardError):
	pass

class PlacesAPI:
	_key = ''
	_root = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?sensor=false'

	def query(self, location='', radius='', keywords='', pagetoken='', timeout=timedelta(seconds=20), url='', verbose=False):
		if url: # Get a premade connection string
			url_copy = url
		else: # Build the connection string
			if not location:
				raise ValueError('Location was not specified and no connection string was provided')
			if not radius:
				raise ValueError('Radius was not specified and no connection string was provided')
			url = self._root
			url += '&key=' + self._key
			url += '&location=' + location
			url += '&radius=' + radius
			if keywords:
				url += '&keyword=' + keywords
			url_copy = url # Save url without the pagetoken for recursion
		if pagetoken:
			url += '&pagetoken=' + pagetoken

		# Print verbose information
		if verbose:
			print 'Querying ' + url

		# Make requests until timeout or success
		decoded = dict([(u'status', u'INVALID_REQUEST')])
		end = datetime.now() + timeout
		while decoded[u'status'] != u'OK' and datetime.now() < end:
			decoded = loads(urlopen(url).read())

		# Handle Places API exceptions
		if decoded[u'status'] != u'OK':
			raise PlacesError('Places API responded with status=' + decoded[u'status'])

		qs = Queryset(decoded[u'results'])

		# Recursively compile pages of results
		try:
			return qs + self.query(pagetoken=decoded[u'next_page_token'], url=url_copy, verbose=verbose)
		except KeyError: # When there is no next page
			return qs

	def __nonzero__(self):
		if self._key:
			return True
		else:
			return False

	def __init__(self, key):
		self._key = key