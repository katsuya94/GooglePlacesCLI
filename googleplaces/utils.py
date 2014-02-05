# Google Places for Python
# Adrien Katsuya Tateno 2014

from string import join
from api import PlacesAPI

# numberp - Errors if numerical conversion is impossible
def numberp(string):
	float(string)

# ezQuery - Handles loosely formatted queries
def ezQuery(api, lat=None, lng=None, radius=None, keywords=[], verbose=False):
	# Validate input
	if api.__class__ != PlacesAPI or not api:
		raise TypeError(api + 'is not a valid PlacesAPI.')
	numberp(lat)
	numberp(lng)
	numberp(radius)

	keywords_str = []

	for keyword in keywords:
		keywords_str.append(str(keyword))

	location = str(lat) + ',' + str(lng)

	# Make request
	return api.query(location, str(radius), join(keywords_str, ','), verbose=verbose)