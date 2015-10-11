"""

    ~~~~~~~~~~~~

    Scrapes NHL time on ice data.

    Copyright: (C) 2015 by Vaisnavan Mahendran
    License: MIT, see LICENSE for more details
"""

class ScrapeTOI:

    def __init__(self, season, game_id):
        self.toi_home = get_toi_home(season, game_id)
        self.toi_visit = get_toi_visit(season, game_id)
        self.home_team_players = []
        self.vist_team_players = []

    def _scrape_header_info(self):
        """Scrapes header information from toi"""

        pass

    def _scrape_home_toi(self):
        """Scrapes home team toi"""

        pass

    def _scrape_visit_toi(self):
        """Scrapes visit team toi"""

        pass
