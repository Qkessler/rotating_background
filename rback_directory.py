import os
import random
import re
from datetime import timedelta
from set_back import set_background

# Fuction that rotates the backgrounds in the path given every
# 'days' days given.

re_format = re.compile(r'.*\.jpg|.*\.png')


def rotating_directory(path, days):
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
        set_background(background, days)
    else:
        random_file = random.randrange(len(images))
        background = images[random_file]
        set_background(background, days)
