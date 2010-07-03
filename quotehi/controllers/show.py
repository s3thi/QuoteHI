import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons import app_globals

from quotehi.lib.base import BaseController, render

log = logging.getLogger(__name__)

class ShowController(BaseController):

    def index(self, id=1):
        self._setup_pagination('quotes', id)
        return render('/index.html')

    def queue(self, id=1):
        self._setup_pagination('quotes.queue', id)
        return render('/queue.html')

    def _setup_pagination(self, db, id):
        quotes_per_page = 10
        quotes_coll = app_globals.db[db]
        c.pages = int((quotes_coll.count() - 1) / quotes_per_page + 1)
        c.current_page = int(id)
        c.quotes = quotes_coll.find().skip(
            (int(id)-1) * quotes_per_page).limit(quotes_per_page)
