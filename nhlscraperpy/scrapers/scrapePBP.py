"""

    ~~~~~~~~~~~~

    Scrapes NHL Play by Play data and returns an object
    containing PBP data.

    Copyright: (C) 2015 by Vaisnavan Mahendran
    License: MIT, see LICENSE for more details
"""

import reqNHLFiles
from lxml import html

class GameEvent:
	"""
	Represents a single game event that occurs in the play by play data
	"""
	
	def __init__(self, events):
		self._event_number = events[0]
		self._period = events[1]
		self._event_strength = events[2]
		self._time_elapsed = events[3]
		self._event = events[4]
		self._description = events[5]
		self._away_on_ice = events[6]
		self._home_on_ice = events[7]

	def get_number(self):

		return self._event_number

	def get_period(self):

		return self._period

	def get_strength(self):
		
		return self._event_strength

	def get_time_elapsed(self):

		return self._time_elapsed

	def get_type(self):

		return self._event

	def get_description(self):

		return self._description

	def get_away_players(self):

		return self._away_on_ice

	def get_home_players(self):

		return self._home_on_ice

class ScrapePBP:

	"""
	Scraper that scrapes play by play nhl data
	"""

	def __init__(self, season, game_id):
		self._season = season
		self._game_id = game_id
		self._events = []

	def scrape_pbp(self):

		dlContent = reqNHLFiles.get_pbp(self._season, self._game_id)
		tree = html.fromstring(dlContent)

		rowEvents = tree.find_class('evenColor')
		
		for event in rowEvents:
			self._events.append(_scrape_row_event(event))


############################## HELPER FUNCTIONS ##############################

def _scrape_row_event(row_event):
	"""
	Helper function to scrape a given event from PBP
	"""

	event_details = row_event.findall('td')
	parsed_event = []

	parsed_event.append(event_details[0].text)
	parsed_event.append(event_details[1].text)
	parsed_event.append(event_details[2].text)
	parsed_event.append(tuple(event_details[3].xpath(".//text()")))
	parsed_event.append(tuple(event_details[4].xpath(".//text()")))
	parsed_event.append(tuple(event_details[5].xpath(".//text()")))

	parsed_event.append(_scrape_row_event_players(event_details[6]))
	parsed_event.append(_scrape_row_event_players(event_details[7]))

	return GameEvent(parsed_event)		

def _scrape_row_event_players(event):
	"""
	Helper function that scrapes the players that were on the ice for a given
	event.
	"""
	
	players = []
	
	for txt in event.xpath(".//text()"):
		if txt != '\r\n' and txt != '\xa0':
			players.append(txt)

	players = list(zip(players[::2], players[1::2]))

	print(players)

	return players
	
		
