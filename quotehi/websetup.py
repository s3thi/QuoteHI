"""Setup the QuoteHI application"""
import logging

import pylons.test
from quotehi.config.environment import load_environment
from quotehi.model.user import User
from getpass import getpass
import random
from hashlib import sha256
from mongokit import Connection


log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup quotehi here"""
    # Don't reload the app if it was loaded under the testing environment
    if not pylons.test.pylonsapp:
        load_environment(conf.global_conf, conf.local_conf)
    
    db_conn = connect(conf)
    db_conn.register([User])
    users_collection = db_conn[conf['mongo.db']].users
    _ = unicode
    
    if usercount(users_collection) == 0:
        print('No existing users found. Creating new user ...')
        
        name = raw_input('Login name for new user: ')
        email = raw_input('Email for new user: ')
        password = getpass('Password for new user: ')
        user = users_collection.User()
        user['name'], user['email'] = _(name), _(email)

        random.seed()
        salt = random.randint(10000000000, 99999999999)
        password = sha256(password + str(salt) + email).hexdigest()

        user['password'], user['salt'] = _(password), _(salt)
        user.save()


def usercount(db):
    return db.find().count()


def connect(conf):
    mongo_host = conf['mongo.host']
    mongo_port = int(conf['mongo.port'])
    mongo_db = conf['mongo.db']
    
    return Connection(mongo_host, mongo_port)

