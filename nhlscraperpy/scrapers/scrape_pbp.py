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

	tree = html.fromstring(pbp_html)

	rows = tree.xpath('//tr[@class="evenColor"]')
	cleaned_data = []

	for row in rows:
		columns = row.findall('td')
		data = [columns[0].text, columns[1].text,
				columns[2].text.replace('\xa0', ""),
		        columns[3].text, columns[4].text,
				columns[5].text.replace('\xa0', " ")]

		visit_players = [player.split('- ')[1]
						 for player in columns[6].xpath('.//td/font/@title')]
		home_players = [player.split('- ')[1]
		 				for player in columns[7].xpath('.//td/font/@title')]

		cleaned_data.append(data + visit_players + home_players)

	return cleaned_data
