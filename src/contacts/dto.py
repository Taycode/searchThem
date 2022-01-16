from flask_restx import fields


def create_contact_dto(api):
    return api.model('Contact', {
        'name': fields.String,
        'phone_number': fields.String,
        'school': fields.String,
        'department': fields.String,
    })
