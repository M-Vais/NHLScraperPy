"""

    scrape_roster.py
    ~~~~~~~~~~~~~~~~
    scrape_roster.py scrapes the roster information. Players are represented
    as a dictionary containing their number, name, and position.
    
    Copyright: (C) 2016 by Vaisnavan Mahendran
    License: MIT, see LICENSE for more details

"""

from lxml import html

def get_home_team(roster_html):

    return (get_home_roster(roster_html), 
            get_home_scratches(roster_html), 
            get_home_coaches(roster_html))

def get_away_team(roster_html):

    return (get_away_roster(roster_html), 
           get_away_scratches(roster_html), 
           get_away_coaches(roster_html))

def get_home_roster(roster_html):

    tree = html.fromstring(roster_html)
    players = tree.xpath('//table[1]/tr/td/table/tr[4]' \
                         '/td/table/tr[1]/td[1]/table/tr')

    return _clean_players(players)

def get_away_roster(roster_html):

    tree = html.fromstring(roster_html)
    players = tree.xpath('//table[1]/tr/td/table/tr[4]' \
                         '/td/table/tr[1]/td[2]/table/tr')

    return _clean_players(players)

def get_home_scratches(roster_html):

    tree = html.fromstring(roster_html)
    scratches = tree.xpath('//*[@id="Scratches"]/td[1]/table/tr')

    return _clean_players(scratches)

def get_away_scratches(roster_html):

    tree = html.fromstring(roster_html)
    scratches = tree.xpath('//*[@id="Scratches"]/td[2]/table/tr')

    return _clean_players(scratches)

def get_home_coaches(roster_html):

    tree = html.fromstring(roster_html)
    coaches = tree.xpath('//*[@id="HeadCoaches"]/td[1]/table/tr')

    return _clean_coaches(coaches)

def get_away_coaches(roster_html):

    tree = html.fromstring(roster_html)
    coaches = tree.xpath('//*[@id="HeadCoaches"]/td[2]/table/tr')

    return _clean_coaches(coaches)  
    
def _clean_players(players):

    roster = []

    for player in players[1:]:
        player_info, player = player.findall('td'), dict()

        player['NAME'] = player_info[2].text.split("(")[0].strip()
        player['POS'] = player_info[1].text
        player['NUM'] = player_info[0].text

        roster.append(player)

    return roster

def _clean_coaches(coaches):

    return [coach.findall('td')[0].text for coach in coaches]
