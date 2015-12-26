"""

	nhlgameroster.py
	~~~~~~~~~~~~~~~~
	nhlgameroster.py contains the roster information of players, officials, 
	coaches in a game.
	
	Copyright: (C) 2015 by Vaisnavan Mahendran
	License: MIT, see LICENSE for more details

"""

from . import nhlrequest
from lxml import html

class ScrapeGameRoster:

	def __init__(self, season, mode, game_id):
		self.season = season
		self.game_id = game_id
		self.mode = mode
		self._rosters = self._scrape()

	def _scrape(self):
		"""
		Scrapes the roster game sheet.
		"""

		roster = {
		 			'HOME': {'ROSTER':[], 'SCRATCHES':[], 'COACHES':[]},
		 			'AWAY': {'ROSTER':[], 'SCRATCHES':[], 'COACHES':[]},
		 			'OFFICIALS': {}
				 }

		html_text = nhlrequest.get_roster(self.season, self.mode, self.game_id)
		tree = html.fromstring(html_text)

		# Home player information
		players = tree.xpath('//table[1]/tr/td/table/tr[4]' \
		                          '/td/table/tr[1]/td[1]/table/tr')
		scratches = tree.xpath('//*[@id="Scratches"]/td[1]/table/tr')
		coaches = tree.xpath('//*[@id="HeadCoaches"]/td[1]/table/tr')

		self._scrape_roster('HOME', players, roster)
		self._scrape_scratches('HOME', scratches, roster)
		self._scrape_coaches('HOME', coaches, roster)

		# Away player information
		players = tree.xpath('//table[1]/tr/td/table/tr[4]' \
		                          '/td/table/tr[1]/td[2]/table/tr')
		scratches = tree.xpath('//*[@id="Scratches"]/td[2]/table/tr')
		coaches = tree.xpath('//*[@id="HeadCoaches"]/td[2]/table/tr')

		self._scrape_roster('AWAY', players, roster)
		self._scrape_scratches('AWAY', scratches, roster)
		self._scrape_coaches('AWAY', coaches, roster)

		return roster

	def get_home_roster(self):
		"""
		Returns the home roster for the game.
		"""

		return self._rosters['HOME']['ROSTER']

	def get_away_roster(self):
		"""
		Returns the away roster for the game.
		"""

		return self._rosters['AWAY']['ROSTER']

	def get_home_scratches(self):
		"""
		Returns scratched players for home team
		"""

		return self._rosters['HOME']['SCRATCHES']

	def get_away_scratches(self):
		"""
		Returns scratched players for away team
		"""

		return self._rosters['AWAY']['SCRATCHES']

	def get_home_coaches(self):
		"""
		Returns coaches for home team
		"""

		return self._rosters['HOME']['COACHES']

	def get_away_coaches(self):
		"""
		Return coaches for away team
		"""

		return self._rosters['AWAY']['COACHES']

	def get_officials(self):
		"""
		Return officials for the game
		"""

		return self._rosters['OFFICIALS']

	def get_home_goalies(self):
		"""
		Returns home goaltenders for the game.
		"""

		return self._get_player_type('HOME', 'G')

	def get_away_goalies(self):
		"""
		Returns away goaltenders for the game.
		"""

		return self._get_player_type('AWAY', 'G')

	def get_home_defenseman(self):
		"""
		Returns home defenders for the game.
		"""

		return self._get_player_type('HOME', 'D')

	def get_away_defenseman(self):
		"""
		Returns away defenders for the game.
		"""

		return self._get_player_type('AWAY', 'D')

	def get_home_forwards(self):
		"""
		Returns home forwards for the game.
		"""

		return self._get_player_type('HOME', 'LRC')

	def get_away_forwards(self):
		"""
		Returns home forwards for the game.
		"""

		return self._get_player_type('AWAY', 'LRC')

############################## HELPER FUNCTIONS ##############################

	def _scrape_roster(self, team, players, roster):
		"""
		Scrapes the players that are playing

		team -- specifying whether its a away or home team
		players -- the xpath for the players
		roster -- the roster to update with player
		"""

		for player in players[1:]:
			player_info = player.findall('td')
			player = {
					  'NAME' : player_info[2].text.split("(")[0].strip(),
					  'POS' : player_info[1].text,
					  'NUM' : player_info[0].text
					 }

			roster[team]['ROSTER'].append(player)

	def _scrape_scratches(self, team, scratches, roster):
		"""
		Scrapes the players that are scratched for that game

		team -- specifying whether its a away or home team
		players -- the xpath for the players
		roster -- the roster to update with player
		"""

		for scratch in scratches[1:]:
			scratch_info = scratch.findall('td')
			scratch = {
					   'NAME' : scratch_info[2].text.split("(")[0].strip(),
					   'POS' : scratch_info[1].text,
					   'NUM' : scratch_info[0].text,
					  }

			roster[team]['SCRATCHES'].append(scratch)

	def _scrape_coaches(self, team, coaches, roster):
		"""
		Scrapes the coaches for the respective teams

		team -- specifying whether its a away or home team
		players -- the xpath for the players
		roster -- the roster to update with player
		"""

		for coach in coaches:
			coach_name = coach.findall('td')[0].text
			roster[team]['COACHES'].append(coach_name)

	def _get_player_type(self, team, type):
		"""
		Filters players with `type`

		team -- whether its an AWAY or HOME team
		type -- indicate the position of player to search
		"""

		players = []

		for player in self._rosters[team]['ROSTER']:
			if player['POS'] in type:
				players.append(player)

		return players


