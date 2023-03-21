from flask_testing import TestCase
from server import create_app
from app.models import db

class BaseTestCase(TestCase):

    def create_app(self):

        app = create_app('testing')
        return app

    def setUp(self):
        
        db.create_all()
        db.session.commit()

    def tearDown(self):

        db.session.remove()
        db.drop_all()
