"""
	scrape_roster.py
	~~~~~~~~~~~~~
	scrape_toi.py scrapes the toi information and returns it in a list of
	list format.

    Copyright: (C) 2016 by Vaisnavan Mahendran
    License: MIT, see LICENSE for more details
"""

from lxml import html

def scrape_toi(toi_html):

	tree = html.fromstring(toi_html)

	players = {}
	player_headings = tree.xpath('//td[@class="playerHeading + border"]')

	for player in player_headings:
		name = _clean_name(player.text)
		players[name] = _scrape_toi(player)

	return players

def _clean_name(name):
	""" Helper function to clean the player name in the html"""

	split_name = name.split(",")
	return split_name[-1].strip() + " " + " ".join(split_name[0].split(" ")[1:])

def _scrape_toi(player_heading):
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
