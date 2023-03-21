from app.models import db
from app.models.model_mixin import ModelMixin

class Url(ModelMixin):

    __tablename__ = 'urls'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, nullable=False)
    slug = db.Column(db.String, nullable=True, unique=True)



