from mongokit import Document
from formencode import Invalid
from formencode.validators import Email, PlainText

def name_validator(name):
    try:
        p = PlainText()
        p.to_python(name)
        return True
    except Invalid:
        return False

def email_validator(email):
    try:
        e = Email()
        e.to_python(email)
        return True
    except Invalid:
        return False

class User(Document):
    structure = {
            'name': unicode,
            'email': unicode,
            'password': unicode
    }

    required_fields = ['name', 'email', 'password']
    validators = {'name': name_validator, 'email': email_validator}
