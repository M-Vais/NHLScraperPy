import requests

def get_html(url):  
    try:
        request = requests.get(url)

        if request.status_code == 200:
            return request.text
        else:
            print('Error 404 - Unable to download: {0}'.format(url))
            return None

    except requests.exceptions.RequestException:
        print('Error - Unable to download: {0}'.format(url))
        return None
