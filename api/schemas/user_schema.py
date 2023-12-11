from api import ma
from ..models import user_model
from marshmallow import fields

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = user_model.User
        load_instance = True
        fields = ("id", "name", "email", "password", "is_admin", "api_key")

    name = fields.String(required=True)
    email = fields.String(required=True)
    password = fields.String(required=True)
    is_admin = fields.Boolean(required=True)
    api_key = fields.String(required=False)
