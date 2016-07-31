from .constants import FILES, SEASONS
import requests

class GameID:

    def __init__(self, season, game_type, game_number):
        self.season = str(season)
        self.game_type = str(game_type).zfill(2)
        self.game_number = str(game_number).zfill(4)

    def season(self):
        return self.season

    def game_type(self):
        return self.game_type

    def game_number(self):
        return self.game_number


def get_url(game_id, filename):

    if filename == 'JSON':
        return FILES[filename].format(game_id.season + game_id.game_type + game_id.game_number)
    else:
        return FILES[filename].format(SEASONS[game_id.season], game_id.game_type, game_id.game_number)


def download_file(game_id, filename):

    return requests.get(get_url(game_id, filename), auth=('user', 'pass'))
