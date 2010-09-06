from mongokit import Connection
from pylons import config


def connect():
    mongo_host = config['mongo.host']
    mongo_port = int(config['mongo.port'])
    mongo_db = config['mongo.db']
    
    return Connection(mongo_host, mongo_port)

def usercount():
    return 0
