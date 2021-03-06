import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons import app_globals

from quotehi.lib.base import BaseController, render
from quotehi.lib.simple_auth import simple_auth
from pymongo import ASCENDING

log = logging.getLogger(__name__)

class ShowController(BaseController):

    def index(self, id=1):
        self._setup_pagination('quotes', id)
        return render('/index.html')

    def queued(self, id=1):
        self._setup_pagination('quotes.queue', id)
        return render('/queue.html')

    @simple_auth
    def flagged(self, id=1):
        self._setup_pagination('quotes', id, flagged=True)
        return render('/flagged.html')

    def _setup_pagination(self, db, id, **kwargs):
        quotes_per_page = 10
        quotes_coll = app_globals.db[db]
        c.current_page = int(id)
        if 'flagged' in kwargs:
            c.quotes = quotes_coll.find({'flagged': kwargs['flagged']}).\
                skip((int(id)-1) * quotes_per_page).\
                limit(quotes_per_page).\
                sort('_id', ASCENDING)
            c.pages = quotes_coll.find({'flagged': kwargs['flagged']}).\
                count()
        else:
            c.quotes = quotes_coll.find().skip(
                (int(id)-1) * quotes_per_page).\
                limit(quotes_per_page).\
                sort('_id', ASCENDING)
            c.pages = int((quotes_coll.count() - 1) / quotes_per_page + 1)
