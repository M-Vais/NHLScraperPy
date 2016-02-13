"""

	nhlgametoi.py
	~~~~~~~~~~~~~
	nhlgametoi.py contains the toi information from a game.
	
    Copyright: (C) 2015 by Vaisnavan Mahendran
    License: MIT, see LICENSE for more details

"""

from lxml import html

def get_toi(toi_html):

	tree = html.fromstring(toi_html)
	player_headings = tree.xpath('//td[@class="playerHeading + border"]')

	return _scrape_toi_players(player_headings)	

def _scrape_toi_players(player_headings):
	"""
	Iterates over each player_heading and fetches player name and its toi
	events.
	"""

	players = {}

	for player_heading in player_headings:
		name = _clean_name(player_heading.text)
		players[name] = _scrape_toi_events(player_heading)

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