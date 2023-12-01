import datetime
from flask import Blueprint, jsonify, request, json
from .sql_strings import Sql_Strings as SQL_STRINGS
from api.utils.misc import val_req_data, handle_error, get_dict_coords
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import CORS
from api.config.conf_mysql import query, sql

mod = Blueprint('users', __name__)
# CORS acces to "users"
CORS(mod)
    
@mod.route('/first_access_by_user_id/<int:id_user>', methods=['GET'])
@jwt_required()
def get_first_access(id_user):
    try:
        if id_user is None:
            return handle_error({'description': 'No se ha enviado el id del usuario','code': 400}), 400
        
        result = query(SQL_STRINGS.GET_FIRST_ACCESS_BY_USER_ID, {'id': id_user}, True)
        if result["status"] == "NOT_FOUND":
            return handle_error({'description': 'No se encontró el usuario con id {}'.format(id_user),'code': 404}), 404
        elif result["status"] != "OK":
            return handle_error({'description': 'No se pudo obtener la información del usuario','code': 500}), 500
        
        print(result["data"])
        return jsonify({
            'status': result["status"],
            'data': {"message": "Se agregó correctamente la imagen", "report_image_details": result["data"]}
        }), 200
    except Exception as e:
        print("Ha ocurrido un error en @first_access_by_user_id/<int:id_user>: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        try:
            e = str(e)
            return handle_error({'description': e[e.find(':')+2:], 'code': int(e[:3])}), int(e[:3])
        except Exception as e:
            return handle_error({'description': "Error inesperado en el servidor", 'code': 500}), 500
        
        
@mod.route('/get_email_exists/<string:email>', methods=['GET'])
def get_email_exists(email):
    try:
        if email is None:
            return handle_error({'description': 'No se ha enviado el email a validar','code': 400}), 400
        
        result = query(SQL_STRINGS.GET_EMAIL, {'email': email}, True)
        if result["status"] == "NOT_FOUND":
            return jsonify({
                'status': result["status"],
                "message": "Correo electrónico disponible"
            }), 200
        elif result["status"] != "OK":
            return handle_error({'description': 'No se pudo obtener la información del usuario','code': 500}), 500
        
        return jsonify({
            'status': result["status"],
            "message": "Correo electrónico no disponible"
        }), 200
    except Exception as e:
        print("Ha ocurrido un error en @get_email_exists/<string:email>: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        try:
            e = str(e)
            return handle_error({'description': e[e.find(':')+2:], 'code': int(e[:3])}), int(e[:3])
        except Exception as e:
            return handle_error({'description': "Error inesperado en el servidor", 'code': 500}), 500