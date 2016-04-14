import requests
from itertools import chain
from .constants import GAME_FILE, SEASONS

def download_html(season, gtype, gnumber, filename):
	""" Downloads the HTML Game data sheets """
	url = GAME_FILE[filename].format(SEASONS[season], gtype, _leftpad(gnumber))

	try:
		html = requests.get(url, auth=('user', 'password'))
		return html.text
	except:
		print("Req. for Season: {0} Game: {1} failed").format(season, gnumber)

def _leftpad(gnumber):
	""" Helper that left pads the gnumber with 0's """
	return (4 - len(str(gnumber))) * '0' + str(gnumber)

def flatten(items):
	""" Given a list of lists flattens the contents into a single list """

	# TODO: Checkout link below
	"http://stackoverflow.com/questions/16176742/python-3-replacement-for-deprecated-compiler-ast-flatten-functiona"

	return list(chain.from_iterable(items))
