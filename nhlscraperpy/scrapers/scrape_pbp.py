"""
	scrape_pbp.py
	~~~~~~~~~~~~~
	scrape_pbp.py scrapes the play by play information and returns it in a list
	of list format.

    Copyright: (C) 2016 by Vaisnavan Mahendran
    License: MIT, see LICENSE for more details
"""

from lxml import html
from ..util import flatten

def scrape_pbp(pbp_html):

	tree = html.fromstring(pbp_html)

	rows = tree.xpath('//tr[@class="evenColor"]')
	cleaned_data = []

	for row in rows:
		columns = row.findall('td')
		data = flatten([columns[0].text, columns[1].text,
				columns[2].text.replace('\xa0', ""),
		        columns[3].text, _parse_event(columns[3].text, columns[4].text),
				columns[5].text.replace('\xa0', " ")])

		visit_players = _clean_player(columns[6].xpath('.//td/font'))
		home_players = _clean_player(columns[7].xpath('.//td/font'))

		cleaned_data.append(data + visit_players + home_players)

	return cleaned_data

def _clean_player(player_columns):
	""" Clean the player name """

	players = []

	for player in player_columns:
		player_name = player.xpath('./@title')[0].split('- ')[1]
		player_number = player.xpath('./text()')[0]

		players.append(player_name + ' ' + player_number)

	return players

def _parse_event(event, description):
	""" Parses the event and return the players involved in the event """

	if (event == 'GOAL'):
		return _parse_shot(description)

	elif (event == 'MISS'):
		return _parse_miss_shot(description)

	elif (event == 'GOAL'):
		return _parse_goal(description)

	elif (event == 'BLOCK'):
		return _parse_block_shot(description)

	elif (event == 'FACEOFF'):
		return _parse_faceoff(description)

	else:
		return description

def _parse_shot(description):

	split = description.split(",")
	shooter = split[0].replace('#', ).split('-').strip()
	zone = split[2]
	distance = split[3]

	return shooter , 'N/A', 'N/A', zone, distance

def _parse_miss_shot(description):

	split = description.split(',')
	shooter = split[0].replace('#', '').split(' ')[1]
	zone = split[2]
	distance = split[3]

	return shooter, 'N/A', 'N/A', zone, distance
