"""

    ~~~~~~~~~~~~

    Scrapes NHL Roster data.

    Copyright: (C) 2015 by Vaisnavan Mahendran
    License: MIT, see LICENSE for more details
"""

class ScrapeRoster:

	def __init__(self, season, game_id):
		self._season = season
		self._game_id = game_id
		self._home_roster = []
		self._away_roster = []

	def scrape_roster(self):

		return downloadNHLFiles.get_roster(self._season, self._game_id)

	def get_home_roster(self):

		return self.home_roster

	def get_away_roster(self):

		return self.away_roster


if __name__ == '__main__':
	
	test = scrapeRoster("20142015", "1")

	result = test.scrape_roster()



