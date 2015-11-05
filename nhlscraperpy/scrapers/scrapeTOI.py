"""

    ~~~~~~~~~~~~

    Scrapes NHL time on ice data.

    Copyright: (C) 2015 by Vaisnavan Mahendran
    License: MIT, see LICENSE for more details
"""

class TOIEvent:
    """
    Represents a single toi event for a player
    """

    def __init__(self, ice_event):
        self._shift = ice_event[0]
        self._period = ice_event[1]
        self._start_shift = ice_event[2]
        self._end_shift = ice_event[3]
        self._duration = ice_event[4]
        self._event = ice_event[5]

class ScrapeTOI:
    """
    Scrapes TOI Information for home and away team
    """
    def __init__(self, season, game_id):
        self._season = season
        self._game_id = game_id
        self._home_team_players = {}
        self._vist_team_players = {}

    def _scrape_home_toi(self, html):
        """Helper function that scrapes the home team toi information"""

        pass

    def _scrape_visit_toi(self, html):
        """Helper function that scrapes the away team toi information """

        pass

    def scrape_toi(self):

        text_toi_home = reqNHLFiles.get_toi_home(self._season, self._game_id)
        text_toi_away = reqNHLFiles.get_toi_away(self._season, self._game_id)
