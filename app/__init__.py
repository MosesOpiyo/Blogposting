from flask import Flask
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()
db = SQLAlchemy


def create_app():
    """
    This is the app factory function
    """
    # Initializing application
    app = Flask(__name__)

from app import views