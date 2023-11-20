from flask_restful import Resource
from main.schemas import UsuarioSchema
from main.services import UsuarioService
from flask import request
from main.utils.handle_errors import serialize_exception

usuario_schema = UsuarioSchema()
usuario_service = UsuarioService()

class UsuarioController(Resource):
    
    def put(self, id):
        try:
            usuario = usuario_service.updateFirstAccess(id)
            return usuario_schema.dump(usuario, many=False)
        except Exception as err:
            return {
                'message': serialize_exception(err),
                'status': 'error'
            }
