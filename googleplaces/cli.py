# Google Places for Python
# Adrien Katsuya Tateno 2014

from argparse import ArgumentParser
from json import loads, dumps
from utils import ezQuery
from queryset import Queryset
from api import PlacesAPI

# Parse command-line input
parser = ArgumentParser()
parser.add_argument('-l', '--location', nargs=2, type=float, help='latitude and longitude of the query (required)', metavar=('latitude', 'longitude'))
parser.add_argument('-r', '--radius', nargs=1, type=float, help='radius of search in meters (required)', metavar='radius')
parser.add_argument('-k', '--keywords', nargs='+', help='search keywords', metavar='keyword')
parser.add_argument('-j', '--json', nargs=1, help='load queries from a json file', metavar='filename')
parser.add_argument('-n', '--names', action='store_true', help='only output names')
parser.add_argument('-v', '--verbose', action='store_true', help='verbose output')
parser.add_argument('key', help='API key provided by Google')
args = parser.parse_args()

api = PlacesAPI(args.key)

if args.json:
	qs = Queryset()
	f = open(args.json[0], 'r')
	queries = loads(f.read())
	for query_dict in queries:
		arg_dict = dict()
		try:
			arg_dict['lat'] = query_dict[u'lat']
			arg_dict['lng'] = query_dict[u'lng']
			arg_dict['radius'] = query_dict[u'radius']
			try:
				arg_dict['keywords'] = query_dict[u'keywords']
			except:
				pass
		except:
			raise str(query_dict) + ' was formatted incorrectly.'
		qs += ezQuery(api, **arg_dict)
else:
	arg_dict = dict()
	try:
		arg_dict['lat'] = args.location[0]
		arg_dict['lng'] = args.location[1]
	except:
		raise SyntaxError('No location provided.')
	try:
		arg_dict['radius'] = args.radius[0]
	except:
		raise SyntaxError('No radius provided.')
	if args.keywords:
		arg_dict['keywords'] = args.keywords
	qs = ezQuery(api, verbose=args.verbose, **arg_dict)
if args.names:
	print dumps(qs.names(), indent=4)
else:
	print dumps(qs.data(), indent=4)