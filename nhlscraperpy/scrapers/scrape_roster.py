"""
	scrape_roster.py
	~~~~~~~~~~~~~
	scrape_roster.py scrapes the roster information and returns it in a list of
	list format.

    Copyright: (C) 2016 by Vaisnavan Mahendran
    License: MIT, see LICENSE for more details
"""

from lxml import html

def scrape_roster(roster_html):
	"""
	Scrapes the roster information and returns a dictionary.
	"""

	tree = html.fromstring(roster_html)

	# visitor and home players
	players = [_clean(tree.xpath('(//td[@class="border"])[1]/table/tr')),
			   _clean(tree.xpath('(//td[@class="border"])[2]/table/tr'))]

	# visitor and home scratches
	scratches = [_clean(tree.xpath('(//td[@class="border"])[3]/table/tr')),
			     _clean(tree.xpath('(//td[@class="border"])[4]/table/tr'))]

	# TODO: Scrape coaching and referee information
	
	return players, scratches

def _clean(players):
	'''
	Helper function to extract information from 'td'.
	'''
	roster = []

	for player in players[1:]:

		player = player.findall('td')
		roster.append((player[2].text.split("(")[0].strip(),
					  player[1].text, player[0].text))
	return roster
