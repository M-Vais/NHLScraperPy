"""
    download.py
    ~~~~~~~~~~~~
    download.py contains functions responsible for downloading html/json files.

    Copyright: (C) 2016 by Vaisnavan Mahendran
    License: MIT, see LICENSE for more details
"""

def get_url(season, mode, game, filename):

    if filename == 'JSON':
        return FILES['JSON'].format(str(season) + str(mode).zfill(2) + \
                                    str(game).zfill(4))
    else:
        return FILES[filename].format(SEASONS[season], str(mode).zfill(2),
                                      str(game).zfill(4))
