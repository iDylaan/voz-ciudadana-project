import datetime
from flask import Blueprint, jsonify, request, json
from .sql_strings import Sql_Strings as SQL_STRINGS
from api.utils.misc import val_req_data, handle_error, get_dict_coords
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import CORS
from api.config.conf_mysql import query, sql
from .schemas import report_schema, report_update_schema, url_image_schema, id_user_schema

mod = Blueprint('users', __name__)
# CORS acces to "users"
CORS(mod)

# CORS Configure Parameters
@mod.route('/first_access_by_user_id', methods=['OPTIONS'])
def handle_options():
    return "", 200, {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE",
        "Access-Control-Allow-Headers": "Content-Type, Authorization"
    }
    
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