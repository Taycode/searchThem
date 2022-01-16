from flask import Flask
from flask_mongoengine import MongoEngine

db = MongoEngine()


def create_app():
    """Creates Flask App"""
    app = Flask(__name__)
    db.init_app(app)
    return app
