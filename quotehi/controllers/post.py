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
            if len(request.POST['quote']) == 0:
                response.status_int = 500
                return 'You must enter a quote.'
            
            quote = self.db.quotes.queue.Quote()
            quote['quote'] = request.POST['quote']
            quote['notes'] = request.POST['notes']
            tags = request.POST['tags'].split()
            quote['tags'] = tags
            quote.save()
        else:
            return render('/add.html')

    def _change_vote(self, by, id):
        if not id in session:
            quote = self.db.quotes.one({'_id': ObjectId(id)})
            quote['votes'] += by
            self.db.quotes.save(quote)
            session[id] = True
            session.save()

    def vote_up(self, id):
            self._change_vote(1, id)

    def vote_down(self, id):
        self._change_vote(-1, id)

    def flag(self, id):
        quote = self.db.quotes.one({'_id': ObjectId(id)})
        quote['flagged'] = True
        self.db.quotes.save(quote)

    def queue(self):
        return 'Queue.'
