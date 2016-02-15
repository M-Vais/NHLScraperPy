"""

	preprocess.py
	~~~~~~~~~~~~~
	preprocess.py is responsible for cleaning the scraped data for further
	use.
	
    Copyright: (C) 2016 by Vaisnavan Mahendran
    License: MIT, see LICENSE for more details

"""


def preprocess_pbp(pbp):

	_generate_player_ids(pbp)
	_process_events(pbp)

	return pbp


def _generate_player_ids(pbp):
	"""
	This replaces player name, number with their player id useful when
	saving to databases, etc. ID is based on player name and birth date.
	"""

	pass


def _process_events(pbp):
	"""
	This processes players that were involved with an event. A maxmium of 3 
	players can be included in an event. For example faceoffs, goals, etc.
	"""
	
	pass


