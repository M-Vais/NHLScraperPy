"""
    constants.py
    ~~~~~~~~~~~~
    constants.py contains important constants used throughout the package.

    Copyright: (C) 2016 by Vaisnavan Mahendran
    License: MIT, see LICENSE for more details
"""

MODE = {

    'PRESEASON' : '1',
    'SEASON' : '2',
    'PLAYOFF' : '3'
}

FILES = {

    # {0} : YYYYZZZZ - YYYY (START_YEAR) - ZZZZ (END_YEAR)
    # {1} : XX (Game Type)
    # {2} : WWWW (Game Number)
<<<<<<< HEAD
    'ROSTER' : 'http://www.nhl.com/scores/htmlreports/{0}/RO{1}{2}.HTM',
    'PBP' : 'http://www.nhl.com/scores/htmlreports/{0}/PL{1}{2}.HTM',
    'TOIV' : 'http://www.nhl.com/scores/htmlreports/{0}/TV{1}{2}.HTM',
    'TOIH' : 'http://www.nhl.com/scores/htmlreports/{0}/TH{1}{2}.HTM',
=======
    'ROSTER' : 'http://www.nhl.com/scores/htmlreports/{0}/RO0{1}{2}.HTM',
    'PBP' : 'http://www.nhl.com/scores/htmlreports/{0}/PL0{1}{2}.HTM',
    'TOIV' : 'http://www.nhl.com/scores/htmlreports/{0}/TV0{1}{2}.HTM',
    'TOIH' : 'http://www.nhl.com/scores/htmlreports/{0}/TH0{1}{2}.HTM',
>>>>>>> 0c37e4b01d3fab7443eef839c40c6b64c5091bb8

    # Contains easy to access information about players playing in games. Will
    # consider doing a full scraper based on JSON in the future.
    # {0} : YYYYXXZZZZ - YYYY (Year) - XX (Game Type) - ZZZZ (Game Number)
    'JSON' : 'https://statsapi.web.nhl.com/api/v1/game/{0}/feed/live'
}

SEASONS = {

<<<<<<< HEAD
    "2007" : "20072008",
    "2008" : "20082009",
    "2009" : "20092010",
    "2010" : "20102011",
    "2011" : "20112012",
    "2012" : "20122013",
    "2013" : "20132014",
    "2014" : "20142015",
    "2015" : "20152016"
=======
    2007 : "20072008",
    2008 : "20082009",
    2009 : "20092010",
    2010 : "20102011",
    2011 : "20112012",
    2012 : "20122013",
    2013 : "20132014",
    2014 : "20142015",
    2015 : "20152016"
>>>>>>> 0c37e4b01d3fab7443eef839c40c6b64c5091bb8
}

TEAMS = {

    "ANA" : "Anaheim Ducks",
    "ARI" : "Arizona Coyotes",
    "BOS" : "Boston Bruins",
    "BUF" : "Buffalo Sabres",
    "CAR" : "Carolina Hurricanes",
    "CBJ" : "Columbus Blue Jackets",
    "CGY" : "Calgary Flames",
    "CHI" : "Chicago Blackhawks",
    "COL" : "Colorado Avalanche",
    "DAL" : "Dallas Stars",
    "DET" : "Detroit Red Wings",
    "EDM" : "Edmonton Oilers",
    "FLA" : "Florida Panthers",
    "LAK" : "Los Angeles Kings",
    "MIN" : "Minnesota Wild",
    "MTL" : "Montreal Canadiens",
    "NJD" : "New Jersey Devil",
    "NSH" : "Nashville Predators",
    "NYI" : "New York Islanders",
    "NYR" : "New York Rangers",
    "OTT" : "Ottawa Senators",
    "PHI" : "Philadelphia Flyers",
    "PIT" : "Pittsburgh Penguins",
    "SJS" : "San Jose Sharks",
    "STL" : "St. Louis Blues",
    "TBL" : "Tampa Bay Lightning",
    "TOR" : "Toronto Maple Leafs",
    "VAN" : "Vancouver Canucks",
    "WPG" : "Winnipeg Jets",
    "WSH" : "Washington Capitals",
    "PHX" : "Phoenix Coyotes",
    "ATL" : "Atlanta Trashers"
}
