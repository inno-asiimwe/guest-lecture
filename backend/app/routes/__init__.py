from flask_restful import Api
from app.controllers import IndexView, UrlsView, RedirectsView




api = Api()

# Index route
api.add_resource(IndexView, '/')
api.add_resource(UrlsView, '/api/v1/shorturl')
api.add_resource(RedirectsView, '/<string:slug>')