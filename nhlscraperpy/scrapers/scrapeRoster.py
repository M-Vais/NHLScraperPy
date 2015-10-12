"""
	nhlscraperpy.scrapers.scrapeRoster
    ~~~~~~~~~~~~

    Scrapes NHL Roster data.

    Copyright: (C) 2015 by Vaisnavan Mahendran
    License: MIT, see LICENSE for more details
"""

import reqNHLFiles
from lxml import html

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
						 		   "coaches" : []},

						 "referees" : [], "linesmen" : []
						}

	def get_home_roster(self):
		"""Returns a dictionary of home team roster information"""

		return self._rosters['home']

	def get_away_roster(self):
		"""Returns a dictionary of away team roster information"""

		return self._rosters['away']

	def scrape_roster(self):
		"""Scrapes the rosters and sets roster info"""

		# get roster information for the specific game
		dlContent = reqNHLFiles.get_roster(self._season, self._game_id)
		tree = html.fromstring(dlContent)

		# home team roster
		home_players = tree.xpath('//html/body/table[1]/tr/td/table/tr[4]' \
		                          '/td/table/tr[1]/td[1]/table/tr')
		home_scratches = tree.xpath('//*[@id="Scratches"]/td[1]/table/tr')
		home_coaches = tree.xpath('//*[@id="HeadCoaches"]/td[1]/table/tr')

		self._scrape_playing_roster("home", home_players)
		self._scrape_scratches("home", home_scratches)
		self._scrape_coaches("home", home_coaches)

		# away team roster
		away_players = tree.xpath('//html/body/table[1]/tr/td/table/tr[4]' \
		                          '/td/table/tr[1]/td[2]/table/tr')
		away_scratches = tree.xpath('//*[@id="Scratches"]/td[2]/table/tr')
		away_coaches = tree.xpath('//*[@id="HeadCoaches"]/td[2]/table/tr')

		self._scrape_playing_roster("away", away_players)
		self._scrape_scratches("away", away_scratches)
		self._scrape_coaches("away", away_coaches)


############################## HELPER FUNCTIONS ##############################

	def _scrape_playing_roster(self, team, players):
		"""Scrapes the players that are playing"""

		for player in players[1:]:
			player_attributes = player.findall('td')
			player = {
					  "name" : player_attributes[2].text,
					  "pos" : player_attributes[1].text,
					  "num" : player_attributes[0].text
					 }

			self._rosters[team]["playing"].append(player)

	def _scrape_scratches(self, team, scratches):
		""" Scrapes the players that are scratched for that game """

		for scratch in scratches[1:]:
			scratch_attributes = scratch.findall('td')
			scratch = {
					   "name" : scratch_attributes[2].text,
					   "pos" : scratch_attributes[1].text,
					   "num" : scratch_attributes[0].text,
					  }

			self._rosters[team]["scratches"].append(scratch)

	def _scrape_coaches(self, team, coaches):
		""" Scrapes the coaches for the respective teams """

		for coach in coaches:
			coach_name = coach.findall('td')[0].text
			self._rosters[team]["coaches"].append(coach_name)
