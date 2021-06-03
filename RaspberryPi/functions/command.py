# command

import subprocess

def command(command):
    if type(command) == str:
        result = subprocess.check_output(command)
        return result.decode(encoding = 'utf-8')
    elif type(command) == list:
        for cmd in command:
            if type(cmd) != str:
                return None
        result = subprocess.check_output(command)
        return result.decode(encoding = 'utf-8')
    else:
        return None

