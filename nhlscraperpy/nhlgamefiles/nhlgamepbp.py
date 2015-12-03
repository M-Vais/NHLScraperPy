"""

	nhlgamepbp.py
	~~~~~~~~~~~~
	nhlgamepbp.py contains the play by play information for the game.
	
    Copyright: (C) 2015 by Vaisnavan Mahendran
    License: MIT, see LICENSE for more details

"""

from . import nhlrequest
from lxml import html

class NHLGamePBP:

	def __init__(self, season, mode, game_id):
		self.season = season
		self.mode = mode
		self.game_id = game_id
		self._pbp = self._scrape()

	def _scrape(self):
		"""
		Scrapes the play by play sheet.
		"""

		pbp = nhlrequest.get_pbp(self.season, self.mode, self.game_id)
		tree = html.fromstring(pbp)

		events = tree.xpath("//tr[@class='evenColor']")
		pbp_events = []

		for event in events:
			descriptions = event.xpath("./td/text()")[:7]
			away_on_ice = event.xpath("td[7]//font/@title")
			home_on_ice = event.xpath("td[8]//font/@title")

			descriptions.append(_clean_on_ice(away_on_ice))
			descriptions.append(_clean_on_ice(home_on_ice))	
			pbp_events.append(descriptions)

		return pbp_events		

############################## HELPER FUNCTIONS ##############################

def _clean_on_ice(players_on_ice):
	"""
	Helper that cleans the player information for whose on the ice to
	only have their names.
	"""

	players = []

	for player in players_on_ice:
		players.append(player.split("-")[1].strip())

	return players