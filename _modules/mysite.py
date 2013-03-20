def syncdb():
    command = "syncdb"
    SETTINGS = "autoroute.prod"
    BIN_ENV = "/home/django/treadhub.com"
    PYTHONPATH = "/home/django/treadhub.com/src/leadville/"

    return __salt__['django.command'](
        SETTINGS, command, BIN_ENV, PYTHONPATH)


def migrate():
    command = "migrate"
    SETTINGS = "autoroute.prod"
    BIN_ENV = "/home/django/treadhub.com"
    PYTHONPATH = "/home/django/treadhub.com/src/leadville/"

    return __salt__['django.command'](
        SETTINGS, command, BIN_ENV, PYTHONPATH)


def collectstatic():
    SETTINGS = "autoroute.prod"
    BIN_ENV = "/home/django/treadhub.com"
    PYTHONPATH = "/home/django/treadhub.com/src/leadville/"

    return __salt__['django.collectstatic'](
        SETTINGS, BIN_ENV, pythonpath=PYTHONPATH)


def restart_apache():
    return __salt__['apache.signal']('restart')


def restart_supervisord():
    return __salt__['cmd.run']('service supervisord restart')


def update_code():
    return __salt__['git.pull']('/home/django/treadhub.com/src/leadville/')


def backup_db():
    cmd = 'pg_dump treadhub | gzip > /tmp/$(date +"%Y-%m-%d").dump.gz'
    cwd = '/home/django'
    runas = 'django'
    return __salt__['cmd.run'](cmd, cwd=cwd, runas=runas)


def quick_deploy():
    return update_code(), collectstatic(), restart_apache(), restart_supervisord()


def full_deploy():
    return backup_db(), update_code(), migrate(), collectstatic(), restart_apache(), restart_supervisord()

