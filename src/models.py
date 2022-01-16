from . import db


class Contact(db.Document):
    """User Model"""
    name = db.StringField()
    phone_number = db.StringField()
    school = db.StringField()
    department = db.StringField()
