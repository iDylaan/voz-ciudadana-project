from flask_restful import Resource
from main.schemas import UsuarioSchema
from main.services import UsuarioService
from flask import request, jsonify
from main.utils.handle_errors import serialize_exception
from .. import db
from main.models import UsuarioModel

usuario_schema = UsuarioSchema()
usuario_service = UsuarioService()

class UsuarioController(Resource):
    
    def put(self, id):
        usuario = db.session.query(UsuarioModel).get(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(usuario, key, value)
        try:
            db.session.add(usuario)
            db.session.commit()
            return usuario.to_json(), 201
        except:
            db.session.rollback()
            return {
                "message":"Ocurrio un error al intentar actualizar el usuairo",
                "status": "error"
            },505
        finally:
            db.session.close()
        # try:
        #     usuario = usuario_service.updateFirstAccess(id)
        #     return usuario_schema.dump(usuario, many=False)
        # except Exception as err:
        #     return {
        #         'message': serialize_exception(err),
        #         'status': 'error'
        #     }
