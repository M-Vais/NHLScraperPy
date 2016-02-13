"""

	nhlgamepbp.py
	~~~~~~~~~~~~~
	nhlgamepbp.py contains the play by play information for the game.
	
    Copyright: (C) 2015 by Vaisnavan Mahendran
    License: MIT, see LICENSE for more details

"""

from lxml import html

def get_pbp(pbp_html):

	tree = html.fromstring(pbp_html)

	pbp_events = []

	for event in tree.xpath("//tr[@class='evenColor']"):
		descriptions = _clean_description(event.xpath("./td/text()")[:7])
		away_players = _clean_players(event.xpath("td[7]//font/@title"))
		home_players = _clean_players(event.xpath("td[8]//font/@title"))

		pbp_events.append(descriptions + away_players + home_players) 

	return pbp_events		

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


def _clean_players(players_on_ice):
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