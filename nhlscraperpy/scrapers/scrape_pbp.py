"""
    scrape_pbp.py
    ~~~~~~~~~~~~~
    scrape_pbp.py scrapes the play by play information and returns it in a list
    of list format.

    Copyright: (C) 2016 by Vaisnavan Mahendran
    License: MIT, see LICENSE for more details
"""
from lxml import html

def scrape_pbp(pbp_html):

    data = []
    tree = html.fromstring(pbp_html)
    
    for row in tree.xpath('//tr[@class="evenColor"]'):

        cols = row.findall('td')
        info = [cols[0].text, cols[1].text, cols[2].text.replace('\xa0', ""),
                cols[3].text, cols[4].text,
                cols[5].text.replace('\xa0', " ").replace(",", "-")]

        visit_players = _clean_player(cols[6].xpath('.//td/font'))
        home_players = _clean_player(cols[7].xpath('.//td/font'))

        data.append(info + visit_players + home_players)

    return data
''' ~~~~~~~~~~~~~~~~~~~~~~~~~~ HELPER FUNCTIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~ '''

def _clean_player(player_columns):
    """ Clean the player name """

    players = []

    for player in player_columns:
        player_name = player.xpath('./@title')[0].split('- ')[1]
        #player_number = player.xpath('./text()')[0]
        print()
        players.append(player_name)

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
