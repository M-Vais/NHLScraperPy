from nhlscraperpy.scrapers import scrape_pbp
from nhlscraperpy import util

def generatePBPCSV(year, game_type, game_number):

    pbp = scrape_pbp.scrape_pbp(util.download_html(year, game_type, game_number, 'PBP'))

    with open("{0}-{1}-{2}PBP.csv".format(year, game_type, game_number), "w+") as output:

        output.write("#, Per, Str, Time Elapsed, Event, Description, P11, P12, P13, P14, P15, G11, P21, P22, P23, P24, P25, G26\n")

        for row in pbp:
            output.write(','.join(row) + "\n")

if __name__ == '__main__':
    generatePBPCSV(2015, 2, 1)
