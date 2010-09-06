from mongokit import Document
import datetime


class Quote(Document):
    structure = {
            'quote': unicode,
            'notes': unicode,
            'tags': list,
            'votes': int,
            'submitted': datetime.datetime
    }

    required_fields = ['quote', 'votes', 'submitted']
    default_values = {'votes': 0, 'submitted': datetime.datetime.utcnow}
