from src import db


class Contact(db.Document):
    """User Model"""
    name = db.StringField()
    phone_number = db.StringField()
    school = db.StringField()
    department = db.StringField()

    def to_json(self):
        """Returns JSON format of model instance"""
        return {
            'name': self.name,
            'phone_number': self.phone_number,
            'school': self.school,
            'department': self.department
        }
