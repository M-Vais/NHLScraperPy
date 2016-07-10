"""

	Constants.py
	~~~~~~~~~~~~
	Constants.py contains important constants used throughout the package.

    Copyright: (C) 2016 by Vaisnavan Mahendran
    License: MIT, see LICENSE for more details
"""

MODE = {
	'PRESEASON' : '1',
	'SEASON' : '2',
	'PLAYOFF' : '3'
}

GAME_FILE = {
	# {0} : YYYYZZZZ - YYYY (START_YEAR) - ZZZZ (END_YEAR)
	# {1} : XX (Game Type)
	# {2} : WWWW (Game Number)
    'ROSTER' : 'http://www.nhl.com/scores/htmlreports/{0}/RO0{1}{2}.HTM',
    'PBP' : 'http://www.nhl.com/scores/htmlreports/{0}/PL0{1}{2}.HTM',
    'TOIV' : 'http://www.nhl.com/scores/htmlreports/{0}/TV0{1}{2}.HTM',
    'TOIH' : 'http://www.nhl.com/scores/htmlreports/{0}/TH0{1}{2}.HTM',

    # Contains easy to access information about players playing in games. Will
	# consider doing a full scraper based on JSON in the future.
	# {0} : YYYYXXZZZZ - YYYY (Year) - XX (Game Type) - ZZZZ (Game Number)
	'JSON' : 'https://statsapi.web.nhl.com/api/v1/game/{0}/feed/live'
}

SEASONS = {
	2007 : "20072008",
	2008 : "20082009",
	2009 : "20092010",
	2010 : "20102011",
	2011 : "20112012",
	2012 : "20122013",
	2013 : "20132014",
	2014 : "20142015",
	2015 : "20152016"
}
