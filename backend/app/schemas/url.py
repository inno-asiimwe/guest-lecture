from marshmallow import Schema, fields, validate

class UrlSchema(Schema):

    url = fields.Url(required=True, schemes=['http', 'https'])
    slug = fields.String(dump_only=True)
    shortlink = fields.Url(dump_only=True)