"""

	nhlgameroster.py
	~~~~~~~~~~~~~~~~
	nhlgameroster.py contains the roster information of players, officials, 
	coaches in a game.
	
	Copyright: (C) 2015 by Vaisnavan Mahendran
	License: MIT, see LICENSE for more details

"""

from ..util.nhlrequest import get_roster
from lxml import html

class ScrapeRoster:

	def __init__(self, season, game_type, game_number):
		self._html = get_roster(season, game_type, game_number)

	def scrape(self):
		"""
		Scrapes the roster game sheet.
		"""

		roster = {
		 			'HOME': {'ROSTER':[], 'SCRATCHES':[], 'COACHES':[]},
		 			'AWAY': {'ROSTER':[], 'SCRATCHES':[], 'COACHES':[]},
		 			'OFFICIALS': {}
				 }

		tree = html.fromstring(self._html)

		# Home player information
		players = tree.xpath('//table[1]/tr/td/table/tr[4]' \
		                          '/td/table/tr[1]/td[1]/table/tr')
		scratches = tree.xpath('//*[@id="Scratches"]/td[1]/table/tr')
		coaches = tree.xpath('//*[@id="HeadCoaches"]/td[1]/table/tr')

		roster = _scrape_roster('HOME', players, roster)
		roster = _scrape_scratches('HOME', scratches, roster)
		roster = _scrape_coaches('HOME', coaches, roster)

		# Away player information
		players = tree.xpath('//table[1]/tr/td/table/tr[4]' \
		                          '/td/table/tr[1]/td[2]/table/tr')
		scratches = tree.xpath('//*[@id="Scratches"]/td[2]/table/tr')
		coaches = tree.xpath('//*[@id="HeadCoaches"]/td[2]/table/tr')

		roster = _scrape_roster('AWAY', players, roster)
		roster = _scrape_scratches('AWAY', scratches, roster)
		roster = _scrape_coaches('AWAY', coaches, roster)

		return roster

############################## HELPER FUNCTIONS ##############################

def _scrape_roster(team, players, roster):
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

	return roster

def _scrape_scratches(team, scratches, roster):
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

	return roster

def _scrape_coaches(team, coaches, roster):
	"""
	Scrapes the coaches for the respective teams

	team -- specifying whether its a away or home team
	players -- the xpath for the players
	roster -- the roster to update with player
	"""

	for coach in coaches:
		coach_name = coach.findall('td')[0].text
		roster[team]['COACHES'].append(coach_name)

	return roster

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


