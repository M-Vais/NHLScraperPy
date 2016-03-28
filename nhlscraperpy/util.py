import requests
from .constants import GAME_FILE, SEASONS

def download_pbp(season, gtype, gnumber):

	return download_html(season, gtype, gnumber, 'PBP')

def download_roster(season, gtype, gnumber):

	return download_html(season, gtype, gnumber, 'ROSTER')

def download_toi(season, gtype, gnumber):

	return download_html(season, gtype, gnumber, 'TOIV'), download_html(season, gtype, gnumber, 'TOIH')

def download_html(season, gtype, gnumber, filename):

	url = GAME_FILE[filename].format(SEASONS[season], gtype, _leftpad(gnumber))

	try: 
		r = requests.get(url, auth=('user', 'password'))
		
		return r.text
	except:
		print("Req. for Season: {0} Game: {1} failed").format(season, gnumber)

def _leftpad(gnumber):

	return (4 - len(str(gnumber))) * '0' + str(gnumber)

