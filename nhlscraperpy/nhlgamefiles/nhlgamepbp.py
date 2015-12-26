"""

	nhlgamepbp.py
	~~~~~~~~~~~~~
	nhlgamepbp.py contains the play by play information for the game.
	
    Copyright: (C) 2015 by Vaisnavan Mahendran
    License: MIT, see LICENSE for more details

"""

from . import nhlrequest
from lxml import html

class ScrapeGamePBP:

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

		
			descriptions = _clean_description(descriptions)
			descriptions.extend(_clean_on_ice(away_on_ice))
			descriptions.extend(_clean_on_ice(home_on_ice))	
			pbp_events.append(descriptions)

		return pbp_events		

############################## HELPER FUNCTIONS ##############################

def _clean_description(descriptions):
	"""
	Helper that cleans and remove certain strings from the descriptions
	like '\xa0' which are replace with None or " ".
	"""
	for index, description in enumerate(descriptions):

		if index == 2 and '\xa0' == description:
			descriptions[index] = None

		elif '\xa0' in description:
			descriptions[index] = descriptions[index].replace('\xa0', " ")

	return descriptions


def _clean_on_ice(players_on_ice):
	"""
	Helper that cleans the player information for whose on the ice to
	only have their names.
	"""

	players = []

	# Gets only the player name 
	for player in players_on_ice:
		players.append(player.split("-")[1].strip())

	# Insert None for slots when there are less than 6 players on ice
	# To ensure consistency for the length of the players
	while len(players) < 6:
		players.insert(-1, None)

	return players