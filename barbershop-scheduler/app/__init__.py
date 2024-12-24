from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'mysecretkey')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
                                                    'DATABASE_URI',
                                                    'sqlite:///barbershop.db')
    app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # from .routes import main
    # app.register_blueprint(main)

    return app