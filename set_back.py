import os
import datetime
import re
import logbook

app_log = logbook.Logger('App')


def set_background(background, days=0):
    last_background = None
    with open('backgrounds.log', 'r') as f:
        last_background = f.readline().strip('\n')
    if last_background:
        today = datetime.today()
        pat = re.compile(r'\d+-\d+-\d+')
        date_str = pat.findall(last_background)
        date = datetime.strptime(date_str[0], '%Y-%m-%d').date()
        if today.date() >= date + days:
            command_log(background)
    else:
        command_log(background)


def command_log(background):
    command = 'gsettings set org.gnome.desktop.background picture-uri "'
    command = "".join([command, background])
    command = command + '"'
    os.system(command)
    os.system('echo -n "" > backgrounds.log')
    app_log.trace(f'Set background: {background}')
