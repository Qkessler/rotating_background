from logging_file import init_logging
from rback_directory import rotating_directory
from rback_api import rotating_api
import os.path

if __name__ == '__main__':
    init_logging('backgrounds.log')
    mode = 'a'
    if mode == 'd':
        if os.path.isfile('input_user.txt'):
            with open('input_user.txt', 'r') as f:
                lines = f.readlines()
                rotating_directory(lines[0].strip('\n'), lines[1].strip('\n'))
        else:
            path = input('Type the absolute path of the wallpapers:\n')
            days = input('Type in how many days you want to change it:\n')
            with open('input_user.txt', 'w') as f:
                f.write(path + '\n')
                f.write(days + '\n')
    else:
        rotating_api('loquesea')
