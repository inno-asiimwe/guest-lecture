import os
from os.path import join, dirname

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from app.routes import api
from app.models import db

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

def create_app(environment):

    from config.config import app_config

    app = Flask(__name__)
    migrate = Migrate()

    app.config.from_object(app_config[environment])

    CORS(app)

    api.init_app(app)

    db.init_app(app)
    
    migrate.init_app(app, db)

    return app

app = create_app(os.getenv('FLASK_ENV'))

if __name__ == '__main__':
    app.run()

