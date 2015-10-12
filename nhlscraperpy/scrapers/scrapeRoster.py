"""
	nhlscraperpy.scrapers.scrapeRoster
    ~~~~~~~~~~~~

    Scrapes NHL Roster data.

    Copyright: (C) 2015 by Vaisnavan Mahendran
    License: MIT, see LICENSE for more details
"""

import downloadNHLFiles

class ScrapeRoster:
	"""
	Scrapes roster info
	"""

	def __init__(self, season, game_id):
		self._season = season
		self._game_id = game_id
		self._rosters = {
						 "home" : {"playing" : [], "scratches" : [], 
						 		   "coaches" : []},

						 "away" : {"playing" : [], "scratches" : [], 
						 		   "coaches" : []}
						}


	def scrape_roster(self):
		"Scrapes the rosters and sets roster info"
		# get roster information for the specific game
		page = downloadNHLFiles.get_roster(self._season, self._game_id)


	def get_home_roster(self):

		return self._rosters['home']

	def get_away_roster(self):

		return self._rosters['away']