"""

	Constants.py
	~~~~~~~~~~~~
	Constants.py contains important constants used throughout the package.
	
    Copyright: (C) 2015 by Vaisnavan Mahendran
    License: MIT, see LICENSE for more details

"""

MODE = {
	
	'PRESEASON' : '1',
	'SEASON' : '2',
	'PLAYOFF' : '3'
}

GAME_FILES = {

    'ROSTER' : 'http://www.nhl.com/scores/htmlreports/{0}/RO0{1}{2}.HTM',
    'PBP' : 'http://www.nhl.com/scores/htmlreports/{0}/PL0{1}{2}.HTM',
    'TOIV' : 'http://www.nhl.com/scores/htmlreports/{0}/TV0{1}{2}.HTM',
    'TOIH' : 'http://www.nhl.com/scores/htmlreports/{0}/TH0{1}{2}.HTM'

}

SEASONS = {
	
	2012 : "20112012",
	2013 : "20122013",
	2014 : "20132014",
	2015 : "20142015",
	2016 : "20152016"
}

REG_SEASON_GAMES = 1230




