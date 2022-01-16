from flask_restx import Namespace, Resource
from flask import request
from src.contacts.models import Contact
from src.contacts.dto import create_contact_dto

contacts_namespace = Namespace('Contacts', 'Contacts Module')


@contacts_namespace.route('/create')
class CreateContact(Resource):
    """Resource for Creating Contact"""
    @contacts_namespace.expect(create_contact_dto(contacts_namespace))
    def post(self):
        payload = request.json
        contact = Contact(**payload).save()
        return contact.to_json()
