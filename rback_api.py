import os
import requests
from set_back import command_log, set_background

ACCESS_KEY = os.environ['ACCESS_KEY']
SECRET_KEY = os.environ['SECRET_KEY']
REDIRECT_URI = os.environ['REDIRECT_URI']
ABSOLUTE_PATH = os.environ['ABSOLUTE_PATH']

headers = {'Accept-Version': 'v1',
           'Authorization': f'Client-ID {ACCESS_KEY}'}


base = 'https://api.unsplash.com/photos/random'


def rotating_api(keyword):
    params = {'query': 'landscape',
              'orientation': 'landscape'}
    res = requests.get(base, params=params, headers=headers)
    data = res.json()
    download_link = data['links']['download']
    content = requests.get(download_link)
    with open('api_files/file1.jpg', 'wb') as f:
        f.write(content.content)
    set_background(ABSOLUTE_PATH)


if __name__ == '__main__':
    rotating_api('wallpaper', 3)
