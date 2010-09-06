from mongokit import Document
from formencode import Invalid
from formencode.validators import Email

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
    validators = {'email': email_validator}
