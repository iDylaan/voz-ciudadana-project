from marshmallow import Schema, fields, post_load, post_dump, ValidationError
from main.models import UsuarioModel

class UsuarioSchema(Schema):
    id = fields.Integer(dump_only = True)
    email = fields.String(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
    is_admin = fields.Boolean(requiered=True)
    is_active = fields.Boolean(requiered=True)
    profile_picture = fields.Integer(required = True)
    profile_banner = fields.Integer(required = True)
    first_access = fields.Boolean(requiered=True)

    @post_load
    def create_user(self, data, **kwargs):
        return UsuarioModel(**data)
    
    SKIP_VALUES = ['password']

    @post_dump
    def remove_skip_values(self, data, **kwargs):
        return {
            key: value for key, value in data.items() if key not in self.SKIP_VALUES
        }