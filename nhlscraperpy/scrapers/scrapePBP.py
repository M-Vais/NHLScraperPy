"""

	nhlgamepbp.py
	~~~~~~~~~~~~~
	nhlgamepbp.py contains the play by play information for the game.
	
    Copyright: (C) 2015 by Vaisnavan Mahendran
    License: MIT, see LICENSE for more details

"""

from ..util.nhlrequest import get_pbp
from lxml import html

class ScrapePBP:

	def __init__(self, season, game_type, game_number):
		self._html = get_pbp(season, game_type, game_number)

	def scrape(self):
		"""
		Scrapes the play by play sheet.
		"""
		tree = html.fromstring(self._html)

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

	def get_html(self):
		"""
		Returns HTML of the PBP
		"""

		return self._html		

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
	# To ensure consistency for the number of the players on the ice
	while len(players) < 6:
		players.insert(-1, None)

	return players