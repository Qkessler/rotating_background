from logging_file import init_logging
from rotating_back import rotating_background
import os.path

if __name__ == '__main__':
    init_logging('backgrounds.log')
    if os.path.isfile('input_user.txt'):
        with open('input_user.txt', 'r') as f:
            lines = f.readlines()
            rotating_background(lines[0], lines[1])
    else:
        path = input('Type the absolute path of the wallpapers:\n')
        days = input('Type in how many days you want to change it:\n')
        with open('input_user.txt', 'w') as f:
            f.write(path + '\n')
            f.write(days)
