import datetime
from flask import Blueprint, jsonify, request, json
from .sql_strings import Sql_Strings as SQL_STRINGS
from api.utils.misc import val_req_data, handle_error, get_dict_coords
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import CORS
from api.config.conf_mysql import query, sql

mod = Blueprint('categories', __name__)
# CORS acces to "reports"
CORS(mod)

# CORS Configure Parameters
@mod.route('/categories', methods=['OPTIONS'])
def handle_options():
    return "", 200, {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE",
        "Access-Control-Allow-Headers": "Content-Type, Authorization"
    }
    
# =========== ENDPOINTS ===========
@mod.route('/categories', methods=['GET'])
@jwt_required()
def get_categories():
    try:
        result = query(SQL_STRINGS.GET_CATEGORIES)
        if result["status"] == "NOT_FOUND":
            return handle_error({'description': 'No hay resultados de categorias','code': 404}), 404
        elif result["status"] != "OK":
            return handle_error({'description': 'No se pudo obtener los resultados de categorias','code': 500}), 500
        
        categories_dict = [dict(row) for row in result["data"]]
        return jsonify({
            'status': result["status"],
            'data': categories_dict
        }), 200
    except Exception as e:
        print("Ha ocurrido un error en @get_categories/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        try:
            e = str(e)
            return handle_error({'description': e[e.find(':')+2:], 'code': int(e[:3])}), int(e[:3])
        except Exception as e:
            return handle_error({'description': "Error inesperado en el servidor", 'code': 500}), 500