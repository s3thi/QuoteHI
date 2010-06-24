import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons import app_globals
import quotehi.lib.helpers as h

from quotehi.lib.base import BaseController, render

log = logging.getLogger(__name__)

class PostController(BaseController):

    def add(self):
        if len(request.POST) > 0:
            quotes_coll = app_globals.db.quotes
            tags = request.POST['tags'].split()
            quotes_coll.insert({ 'quote': request.POST['quote'],
                                 'tags': tags, 'votes': 1})
            c.submitted = True
            h.redirect(url(controller='post', action='added'))
        
        return render('/add.html')

    def added(self):
        return render('/added.html')

    def vote_up(self):
        return 'Vote up.'

    def vote_down(self):
        return 'Vote down.'

    def report(self):
        return 'Report.'
