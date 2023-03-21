
from sqlalchemy.exc import SQLAlchemyError
from app.models import db

class ModelMixin(db.Model):

    __abstract__ = True

    created_on = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_on = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except SQLAlchemyError:
            db.session.rollback()
            return False

    def flush(self):
        try:
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            return False


    @classmethod
    def find_first(cls, **kwargs):
        try:
            return cls.query.filter_by(**kwargs).first()
        except SQLAlchemyError:
            return False

    @classmethod
    def find_all(cls, **kwargs):
        try:
            return cls.query.filter_by(**kwargs).all()
        except SQLAlchemyError:
            return False

