"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to templates as 'h'.
"""
# Import helpers as desired, or define your own, ie:
#from webhelpers.html.tags import checkbox, password
from pylons import session, url
from pylons.controllers.util import redirect
from webhelpers.html.tags import *
from decorator import decorator

@decorator
def simple_auth(action, *args, **kwargs):
    if session.get('logged_in') is True:
        return action(*args, **kwargs)
    else:
        redirect(url(controller='admin', action='login'))
