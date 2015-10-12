"""

    ~~~~~~~~~~~~

    Scrapes NHL Play by Play data and returns an object
    containing PBP data.

    Copyright: (C) 2015 by Vaisnavan Mahendran
    License: MIT, see LICENSE for more details
"""

class ScrapePBP:

	def __init__(self, season, game_id):
		self._season = season
		self._game_id = game_id
		