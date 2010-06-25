import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons import app_globals
import quotehi.lib.helpers as h

from quotehi.lib.base import BaseController, render
from pymongo.objectid import ObjectId

log = logging.getLogger(__name__)

class PostController(BaseController):

    def add(self):
        if len(request.POST) > 0:
            quotes_coll = app_globals.db.quotes
            tags = request.POST['tags'].split()
            quotes_coll.insert({ 'quote': request.POST['quote'],
                                 'notes': request.POST['notes'],
                                 'tags': tags, 'votes': 1})
            h.redirect(url(controller='post', action='added'))
        
        return render('/add.html')

    def added(self):
        return render('/added.html')

    def _change_vote(self, by, id):
        quotes_coll = app_globals.db.quotes
        quote = quotes_coll.find_one({'_id': ObjectId(id)})
        quote['votes'] += by
        quotes_coll.save(quote)        

    def vote_up(self, id):
        self._change_vote(1, id)

    def vote_down(self, id):
        self._change_vote(-1, id)

    def report(self):
        return 'Report.'
