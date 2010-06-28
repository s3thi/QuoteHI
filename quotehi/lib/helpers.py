"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to templates as 'h'.
"""
# Import helpers as desired, or define your own, ie:
#from webhelpers.html.tags import checkbox, password
from pylons import session, url
from pylons.controllers.util import redirect

def simple_auth(controller):
    def controller_auth(self):
        if session.get('logged_in'):
            controller()
        else:
            redirect(url(controller='admin', action='login'))
    
    return controller_auth
