"""The application's Globals object"""

from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options
from pylons import config
from mongokit import Connection
from quotehi.model import register_models


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
    
        self.connection = Connection(mongo_host, mongo_port)
        self.db = self.connection[mongo_db]
        self.connection.register(register_models)

