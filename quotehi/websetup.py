"""Setup the QuoteHI application"""
import logging

import pylons.test
from quotehi.config.environment import load_environment
import pymongo
from getpass import getpass
from random import random
from hashlib import sha256

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup quotehi here"""
    # Don't reload the app if it was loaded under the testing environment
    if not pylons.test.pylonsapp:
        load_environment(conf.global_conf, conf.local_conf)
    
    mongo_host = conf['mongo.host']
    mongo_db = conf['mongo.db']
    
    try:
        db_conn = pymongo.Connection(mongo_host)
    except pymongo.errors.ConnectionFailure:
        raise Exception('Could not connect to MongoDB.')
    
    db = db_conn[mongo_db]
    email = raw_input('Enter admin email: ')
    password = getpass('Enter password: ')
    salt = int(random() * 10000000000)
    encrypted_password = sha256(password + str(salt) + email).hexdigest()
    db.users.insert({'email': email, 'password': encrypted_password,
                     'salt': salt})
