"""
    nhlscraperpy.scraper.downloadNHLFiles
    ~~~~~~~~~~~~

    Various functions to download related files required for getting the data
    from www.nhl.com.

    Copyright: (C) 2015 by Vaisnavan Mahendran
    License: MIT, see LICENSE for more details
"""

import requests

_FILES = {

    'ROSTER' : 'http://www.nhl.com/scores/htmlreports/{0}/RO02{1}.HTM',
    'PBP' : 'http://www.nhl.com/scores/htmlreports/{0}/PL02{1}.HTM',
    'TOIV' : 'http://www.nhl.com/scores/htmlreports/{0}/TV02{1}.HTM',
    'TOIH' : 'http://www.nhl.com/scores/htmlreports/{0}/TH02{1}.HTM'

}


def get_pbp(season, game_id):
    """ Returns text of html play by play data

    season  -- is composed of the years the season takes place ex. 20142015
    game_id -- indicates a game during nhl season ex. 24
    """

    return _get_html_text(season, game_id, 'PBP')

def get_roster(season, game_id):
    """ Returns text of html roster data of both teams

    season  -- is composed of the years the season takes place ex. 20142015
    game_id -- indicates a game during nhl season ex. 24
    """

    return _get_html_text(season, game_id, 'ROSTER')

def get_toi_home(season, game_id):
    """ Returns text of html time on ice data of the home team

    season  -- is composed of the years the season takes place ex. 20142015
    game_id -- indicates a game during nhl season ex. 24
    """

    return _get_html_text(season, game_id, 'TOIH')

def get_toi_visit(season, game_id):
    """ Returns text of html time on ice data of the visiting team

    season  -- is composed of the years the season takes place ex. 20142015
    game_id -- indicates a game during nhl season ex. 24
    """

    return _get_html_text(season, game_id, 'TOIV')

def _get_html_text(season, game_id, wanted_data):
    """ Returns text format of HTML of wanted_data"""
    
    url = _FILES[wanted_data].format(season, _get_game_id(game_id))

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
