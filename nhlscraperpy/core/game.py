from ..util import download_html
from ..scrapers.scrape_pbp import scrape_pbp
from ..scrapers.scrape_roster import scrape_roster
from ..scrapers.scrape_toi import scrape_toi

class NHLGame:

	def __init__(self, season, gtype, gnumber):
		self.season = season
		self.gtype = gtype
		self.gnumber = gnumber
		self.preprocess()

	def preprocess(self):
		""" Preprocesses the file and sets up for use """

		pass
