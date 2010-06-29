import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons import app_globals
from pylons.controllers.util import abort, redirect

from quotehi.lib.base import BaseController, render
from quotehi.lib.helpers import simple_auth
from hashlib import sha256
from pymongo.objectid import ObjectId

log = logging.getLogger(__name__)

class AdminController(BaseController):

    @simple_auth
    def index(self):
        return 'Admin index.'

    def login(self):
        if len(request.POST) > 0:
            submitted_password = request.POST['password']
            users_coll = app_globals.db.users
            user = users_coll.find_one({'email': request.POST['email']})
            if user:
                salt = user['salt']
                encrypted_password = sha256(submitted_password + str(salt)
                                        + user['email']).hexdigest()
                if user['password'] == encrypted_password:
                    session['logged_in'] = True
                    session['email'] = user['email']
                    session.save()
                    redirect(url(controller='show', action='index'))
        
        return render('/login.html')

    @simple_auth
    def logout(self):
        del session['email']
        del session['logged_in']
        session.save()
        redirect(url(controller='show', action='index'))

    @simple_auth
    def approve(self, id):
        quotes_queue = app_globals.db.quotes.queue
        quote = quotes_queue.find_one({'_id': ObjectId(id)})
        quotes_queue.remove(quote)
        quotes_coll = app_globals.db.quotes
        quotes_coll.insert(quote)

    @simple_auth
    def delete(self, id):
        return 'Deleted.'

    @simple_auth
    def edit(self, id):
        return 'Edit.'

    @simple_auth
    def adduser(self):
        return 'Add new user.'
