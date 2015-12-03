"""

	nhlgametoi.py
	~~~~~~~~~~~~
	nhlgametoi.py contains the toi information from a game.
	
    Copyright: (C) 2015 by Vaisnavan Mahendran
    License: MIT, see LICENSE for more details

"""

from . import nhlrequest
from lxml import html

class NHLGameToi:

	def __init__(self, season, mode, game_id):
		self.season = season
		self.mode = mode
		self.game_id = game_id
		self._home_toi, self._away_toi = self._scrape()

	def _scrape(self):
		"""
		Scrapes the toi roster sheets.
		"""

		home = nhlrequest.get_toi_home(self.season, self.mode, self.game_id) 
		away = nhlrequest.get_toi_away(self.season, self.mode, self.game_id)

		tree = html.fromstring(home)
		player_headings = tree.xpath('//td[@class="playerHeading + border"]')
		home_players = _scrape_toi_players(player_headings)

		tree = html.fromstring(away)
		player_headings = tree.xpath('//td[@class="playerHeading + border"]')
		away_players = _scrape_toi_players(player_headings)

		return home_players, away_players

	def get_home_toi(self):
		"""
		Returns the home team players toi.
		"""

		return self._home_toi

	def get_away_toi(self):
		"""
		Returns the away team players toi.
		"""

		return self._away_toi
		
############################## HELPER FUNCTIONS ##############################


def _scrape_toi_players(player_headings):
	"""
	Iterates over each player_heading and fetches player name and its toi
	events.
	"""

	players = {}

	for player_heading in player_headings:
		name = _clean_name(player_heading.text)
		players[name] = scrape_toi_events(player_heading)

	return players

def _scrape_toi_events(player_heading):
	"""
	Scrapes the toi events for a given player_heading.
	"""

	start = player_heading.getparent().getnext()
	start.set('class', 'start')
	events = start.xpath("./following-sibling::tr[not(@class)][1] \
						   /preceding-sibling::tr \
						   [preceding-sibling::tr[@class='start']]")
	start.set('class', '')

	toi_events = []
	for event in events:
		toi_events.append(event.xpath('./td/text()'))

	return toi_events

def _clean_name(name):
	"""
	Helper function to clean name from player_heading.
	"""

	split_name = name.split(",")	

	return split_name[-1].strip() + " " + " ".join(split_name[0].split(" ")[1:])