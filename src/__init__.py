from flask import Flask
from flask_mongoengine import MongoEngine
from flask_restx import Api

api = Api(title='Contact Searching app', description='A phonebook with a search engine', doc='/docs/')
db = MongoEngine()


def create_app():
    """Creates Flask App"""
    app = Flask(__name__)
    app.config['MONGODB_SETTINGS'] = {
        'db': 'searchThemDb',
        'host': 'mongo',
        'port': 27017
    }
    api.init_app(app)
    db.init_app(app)

    from src.contacts.controllers import contacts_namespace
    api.add_namespace(contacts_namespace, '/contact')
    return app
