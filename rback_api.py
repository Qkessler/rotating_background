import os
import requests
from set_back import set_background

ACCESS_KEY = os.environ['ACCESS_KEY']
SECRET_KEY = os.environ['SECRET_KEY']
REDIRECT_URI = os.environ['REDIRECT_URI']
# code =

headers = {'Accept-Version': 'v1',
           'Authorization': f'Client-ID {ACCESS_KEY}'}


base = 'https://api.unsplash.com/photos/random'


def rotating_api(keyword, days):
    params = {'query': keyword,
              'orientation': 'landscape'}
    res = requests.get(base, params=params, headers=headers)
    data = res.json()
    download_link = data['links']['download']
    content = requests.get(download_link)
    with open('api_files/file1.jpg', 'wb') as f:
        f.write(content.content)
    set_background('api_files/file1.jpg')


if __name__ == '__main__':
    rotating_api('wallpaper', 3)
