import requests
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
