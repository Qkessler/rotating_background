import os
import random
import re
import logbook
from datetime import timedelta, datetime

# Fuction that rotates the backgrounds in the path given every
# 'days' days given.

re_format = re.compile(r'.*\.jpg|.*\.png')
app_log = logbook.Logger('App')


def rotating_background(path, days):
    days = timedelta(days=int(days))
    command = 'gsettings set org.gnome.desktop.background picture-uri "'
    path_files = [f for f in os.listdir(path)]
    abs_path = os.path.abspath(path)
    paths = ["/".join([abs_path, f]) for f in path_files]
    images = [i for i in paths if os.path.isfile(i) and re_format.match(i)]
    last_background = None
    with open('backgrounds.log', 'r') as b:
        last_background = b.readline().strip('\n')
    if last_background:
        background = last_background
        while background in last_background:
            random_file = random.randrange(len(images))
            background = images[random_file]
    else:
        random_file = random.randrange(len(images))
        background = images[random_file]
    today = datetime.today()
    pat = re.compile(r'\d+-\d+-\d+')
    date_str = pat.findall(last_background)
    print(last_background)
    print(date_str)
    date = datetime.strptime(date_str[0], '%Y-%m-%d').date()
    if today.date() >= date + days:
        command = "".join([command, background])
        command = command + '"'
        os.system(command)
        os.system('echo -n "" > backgrounds.log')
        app_log.trace(f'Set background: {background}')
