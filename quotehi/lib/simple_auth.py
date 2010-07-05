from decorator import decorator
from pylons import session, url
from pylons.controllers.util import redirect

@decorator
def simple_auth(action, *args, **kwargs):
    if session.get('logged_in') is True:
        return action(*args, **kwargs)
    else:
        redirect(url(controller='admin', action='login'))
