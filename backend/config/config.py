import os, sys

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
basedir = os.path.abspath(os.path.dirname(__file__))

class Base:

    SECRET_KEY = os.getenv("FLASK_APP_SECRET")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

class Development(Base):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@database/url-shortener"


class Testing(Base):

    TESTING = True
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@test-database/test-database"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.sqlite')


class Staging(Base):

    DEBUG = False
    
class Production(Base):

    DEBUG = False

app_config = {
    "development": Development,
    "testing": Testing,
    "staging": Staging,
    "production": Production 
    }