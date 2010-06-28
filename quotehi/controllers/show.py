import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons import app_globals

from quotehi.lib.base import BaseController, render

log = logging.getLogger(__name__)

class ShowController(BaseController):

    def index(self):
        quotes_coll = app_globals.db.quotes
        quotes = quotes_coll.find().skip(0).limit(10)
        c.quotes = quotes
        return render('index.html')
