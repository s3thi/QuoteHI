"""The application's Globals object"""

from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options
from pylons import config
import pymongo
from pymongo import Connection

class Globals(object):
    """Globals acts as a container for objects available throughout the
    life of the application

    """

    def __init__(self, config):
        """One instance of Globals is created during application
        initialization and is available during requests via the
        'app_globals' variable

        """
        self.cache = CacheManager(**parse_cache_config_options(config))
        mongo_host = config['mongo.host']
        mongo_port = int(config['mongo.port'])
        mongo_db = config['mongo.db']
        
        try:
            self.db_conn = Connection(mongo_host, mongo_port)
        except pymongo.errors.ConnectionFailure:
            raise Exception('Could not connect to MongoDB.')

        self.db = self.db_conn[mongo_db]
