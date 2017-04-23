from fabric.api import run
from fabric.context_managers import settings


def _get_manage_dot_py(host):
    return '~/sites/{}/virtualenv/bin/python ~/sites/{}/source/manage.py'.format(host)


def reset_database(host):
    manage_dot_py = _get_manage_dot_py(host)
    with settings(host_string='ecassan@{}'.format(host)):
        run('{} flush --noinput'.format(manage_dot_py))


def create_session_on_server(host, email):
    manage_dot_py = _get_manage_dot_py(host)
    with settings(host_string='ecassan@{}'.format(host)):
        session_key = run('{} create_session {}'.format(manage_dot_py, email))
        return session_key.strip()
