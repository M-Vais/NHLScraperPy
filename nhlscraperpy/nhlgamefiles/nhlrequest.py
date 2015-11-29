"""

	NHLRequest.py
	~~~~~~~~~~~~
	NHLRequest sends http requests to fetch the requested game files
	and returns it in text format.
	
    Copyright: (C) 2015 by Vaisnavan Mahendran
    License: MIT, see LICENSE for more details

"""

from .. import constants
import requests

def get_pbp(season, mode, game_id):
    """ Returns text of html play by play data

    season  -- is composed of the years the season takes place ex. 20142015
    mode -- is to indicate whether its a preseason, regular, playoff game
    game_id -- indicates a game during nhl season ex. 24
    """

    return _get_html_text(season, mode, game_id, constants.GAME_FILES['PBP'])

def get_roster(season, mode, game_id):
    """ Returns text of html roster data of both teams

    season  -- is composed of the years the season takes place ex. 20142015
    mode -- is to indicate whether its a preseason, regular, playoff game
    game_id -- indicates a game during nhl season ex. 24
    """

    return _get_html_text(season, mode, game_id, constants.GAME_FILES['ROSTER'])

def get_toi_home(season, mode, game_id):
    """ Returns text of html time on ice data of the home team

    season  -- is composed of the years the season takes place ex. 20142015
    mode -- is to indicate whether its a preseason, regular, playoff game
    game_id -- indicates a game during nhl season ex. 24
    """

    return _get_html_text(season, mode, game_id, constants.GAME_FILES['TOIH'])

def get_toi_visit(season, mode, game_id):
    """ Returns text of html time on ice data of the visiting team

    season  -- is composed of the years the season takes place ex. 20142015
    mode -- is to indicate whether its a preseason, regular, playoff game
    game_id -- indicates a game during nhl season ex. 24
    """

    return _get_html_text(season, mode, game_id, constants.GAME_FILES['TOIV'])

def _get_html_text(season, mode, game_id, wanted_data):
    """ Returns text format of HTML of wanted_data

    season  -- is composed of the years the season takes place ex. 20142015
    mode -- is to indicate whether its a preseason, regular, playoff game
    game_id -- indicates a game during nhl season ex. 24
    """
    
    url = wanted_data.format(season, mode, _get_game_id(game_id))

    try:
        r = requests.get(url, auth=('user', 'pass'))
        return r.text

    except:
        print("Req. for Season: {0} Game: {1} failed").format(season, game_id)

def _get_game_id(game_id):
    """ Returns properly formatted game id

    game_id -- a nhl game number that will be properly formatted for use
    """

    NUMBER_OF_ZEROES = 4 - len(str(game_id))

    return "0" * NUMBER_OF_ZEROES + str(game_id)
