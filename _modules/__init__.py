SETTINGS = "autoroute.prod"
BIN_ENV = "/home/django/treadhub.com"
PYTHONPATH = "/home/django/treadhub.com/src/leadville/"

def run_command(command)

    return __salt__['django.command'](
        SETTINGS, command, BIN_ENV, PYTHONPATH)
