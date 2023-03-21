import json
from flask import abort, redirect
from flask_restful import Resource, request
from marshmallow import ValidationError

from app.models.url import Url
from app.schemas import UrlSchema
from app.helpers import generate_slug, generate_short_url


class UrlsView(Resource):

    def post(self):

        url_schema = UrlSchema()

        url_data = request.get_json()

        try:
            validated_url_data = url_schema.load(url_data)

            url = validated_url_data.get("url")
            
            url_exists = Url.find_first(url=url)

            if url_exists:
                url_json = url_schema.dump(url_exists)
                url_json["shortlink"] = generate_short_url(request.host_url, url_json["slug"])

                return dict(status="success", data=url_json), 200

            # generate slug 
            new_url = Url(**validated_url_data)
            new_url.flush()
            new_url.slug = generate_slug(new_url.id, Url)

            saved = new_url.save()

            if not saved:
                return dict(status="fail", message="Internal Server Error"), 500

            new_url_json = url_schema.dump(new_url)
            new_url_json["shortlink"] = generate_short_url(request.host_url, new_url_json["slug"])


            return dict(status="success", data=new_url_json), 201

        except ValidationError as e:
            return dict(status="fail", message=e.messages["url"][0]), 400

        except Exception:
            return dict(status="fail", message="Internal Server Error"), 500

    def get(self):

        url_schema = UrlSchema(many=True)

        try:
            urls = Url.find_all()

            urls_json = url_schema.dump(urls)

            if urls_json:
                for url in urls_json:
                    url["shortlink"] = generate_short_url(request.host_url, url["slug"])

            return dict(status="success", data=urls_json), 200
            
        except Exception:
            return dict(status="fail", message="Internal Server Error"), 500

class RedirectsView(Resource):

    def get(self, slug):

        url = Url.find_first(slug=slug)

        if not url:
            abort(404)

        return redirect(url.url, 302)

