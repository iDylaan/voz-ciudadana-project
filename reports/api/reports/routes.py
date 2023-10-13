import datetime
from flask import Blueprint, jsonify, request
from .sql_strings import Sql_Strings as SQL_STRINGS
from api.utils.misc import val_req_data, handle_error
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import CORS
from api.config.conf_mysql import query, sql
from .schemas import report_schema, report_update_schema

mod = Blueprint('reports', __name__)
# CORS acces to "reports"
CORS(mod)

# CORS Configure Parameters
@mod.route('/reports', methods=['OPTIONS'])
def handle_options():
    return "", 200, {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE",
        "Access-Control-Allow-Headers": "Content-Type, Authorization"
    }

# =========== ENDPOINTS ===========
@mod.route('/reports', methods=['GET'])
def get_reports():
    try:
        result = query(SQL_STRINGS.GET_REPORTS)
        if result["status"] == "NOT_FOUND":
            return handle_error({'description': 'No hay resultados de reportes','code': 404}), 404
        elif result["status"] != "OK":
            return handle_error({'description': 'No se pudo obtener los resultados de reportes','code': 500}), 500
        
        reports_dict = [dict(row) for row in result["data"]]
        for report in reports_dict:
            if report["images"] is not None:
                report["images"] = report["images"].split(",")
            else:
                report["images"] = []
        return jsonify({
            'status': result["status"],
            'data': reports_dict
        }), 200
    except Exception as e:
        print("Ha ocurrido un error en @get_reports/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        try:
            e = str(e)
            return handle_error({'description': e[e.find(':')+2:], 'code': int(e[:3])}), int(e[:3])
        except Exception as e:
            return handle_error({'description': "Error inesperado en el servidor", 'code': 500}), 500



@mod.route('/reports/<int:id_report>', methods=['GET'])
def get_report(id_report):
    try:
        result = query(SQL_STRINGS.GET_REPORT_BY_ID, {'id_report': id_report}, True)
        if result["status"] == "NOT_FOUND":
            return handle_error({'description': 'No se encontró el reporte con id {}'.format(id_report),'code': 404}), 404
        elif result["status"] != "OK":
            return handle_error({'description': 'No se pudo obtener el reporte','code': 500}), 500
        if result["data"]["images"] is not None:
            result["data"]["images"] = result["data"]["images"].split(",")
        else:
            result["data"]["images"] = []
        return jsonify({
            'status': result["status"],
            'data': result["data"]
        }), 200
    except Exception as e:
        print("Ha ocurrido un error en @get_report/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        try:
            e = str(e)
            return handle_error({'description': e[e.find(':')+2:], 'code': int(e[:3])}), int(e[:3])
        except Exception as e:
            return handle_error({'description': "Error inesperado en el servidor", 'code': 500}), 500
    
    
    
@mod.route('/reports', methods=['POST'])
def create_report():
    try:
        data = request.get_json()
        
        # * Validating null values
        title = data.get("title", None)
        description = data.get("description", None)
        user_id = data.get("user_id", None)
        category_id = data.get("category_id", None)
        if not title \
        or not user_id \
        or not category_id:
            missing_data = []
            if title is None:
                missing_data.append({"title": "Titulo del reporte"})
            if user_id is None:
                missing_data.append({"user_id": "ID del usuario que realiza el reporte"})
            if category_id is None:
                missing_data.append({"category_id": "ID de la categoria del reporte"})
            return handle_error({'description': 'Error inesperado en el servidor','code': 400, 'details': {'missing_data': missing_data}}), 400
        
        new_report = {
            "title": title,
            "description": description,
            "user_id": int(user_id),
            "category_id": int(category_id),
            "status_id": 1,
            "images": []
        }
        images = data.get("images", None)
        if images is not None:
            for image in images:
                new_report["images"].append(image)
        
        errors = val_req_data(new_report, report_schema)
        if errors:
            return handle_error({'description': 'Error en la validación de la petición','code': 400, 'details': errors}), 400
        
        result = sql(SQL_STRINGS.INSERT_REPORT, {
            "report_title": new_report['title'],
            "report_description": new_report['description'],
            "user_id": new_report['user_id'],
            "category_id": new_report['category_id'],
            "status_id": new_report['status_id']
        })
        if (result["status"] != "OK"):
            return handle_error({'description': 'Error inesperado en el registro del reporte', 'code': 500}), 500
        
        values_insrt = ''
        for index, image in enumerate(new_report['images']):
            values_insrt += '(\'{}\', {}), '.format(image, result['last_insert_id']) \
                if index < len(new_report['images']) - 1 \
                else '(\'{}\', {})'.format(image, result['last_insert_id'])
        new_report['id'] = result['last_insert_id']
        
        result = sql(SQL_STRINGS.INSERT_REPORT_IMAGES.format(values_insrt))
        if (result["status"] != "OK"):
            return handle_error({'description': 'Error inesperado en el registro de las imagenes del reporte', 'code': 500}), 500
        
        return jsonify({"status": 'OK', "data": new_report}), 200
    except Exception as e:
        print("Ha ocurrido un error en @create_report/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        try:
            e = str(e)
            return handle_error({'description': e[e.find(':')+2:], 'code': int(e[:3])}), int(e[:3])
        except Exception as e:
            return handle_error({'description': "Error inesperado en el servidor", 'code': 500}), 500



@mod.route('/reports/<int:id_report>', methods=['PUT'])
def update_report(id_report):
    try:
        result = query(SQL_STRINGS.GET_REPORT_BY_ID, {'id_report': id_report}, True)
        if result["status"] == "NOT_FOUND":
            return handle_error({'description': 'No se encontró el reporte con id {}'.format(id_report),'code': 404}), 404
        elif result["status"] != "OK":
            return handle_error({'description': 'No se pudo obtener el reporte','code': 500}), 500
        
        old_report = result["data"]
        
        data = request.get_json()
        
        # * Validating null values
        title = data.get("title", None)
        description = data.get("description", None)
        user_id = data.get("user_id", None)
        category_id = data.get("category_id", None)
        if not title \
        or not user_id \
        or not category_id:
            missing_data = []
            if title is None:
                missing_data.append({"title": "Titulo del reporte"})
            if user_id is None:
                missing_data.append({"user_id": "ID del usuario que realiza el reporte"})
            if category_id is None:
                missing_data.append({"category_id": "ID de la categoria del reporte"})
            return handle_error({'description': 'Error inesperado en el servidor','code': 400, 'details': {'missing_data': missing_data}}), 400
        
        new_report = {
            "title": old_report["title"] if title is None else title,
            "description": old_report["report_description"] if description is None else description,
            "category_id": old_report["category_id"] if category_id is None else int(category_id),
        }
        
        errors = val_req_data(new_report, report_update_schema)
        if errors:
            return handle_error({'description': 'Error en la validación de la petición','code': 400, 'details': errors}), 400
        
        result = sql(SQL_STRINGS.UPDATE_REPORT, {
            "report_title": new_report['title'],
            "report_description": new_report['description'],
            "category_id": new_report['category_id'],
            "id_report": id_report
        })
        if (result["status"] != "OK"):
            return handle_error({'description': 'Error inesperado en la actualización del reporte', 'code': 500}), 500
        
        return jsonify({"status": 'OK', "data": new_report}), 200
    except Exception as e:
        print("Ha ocurrido un error en @create_report/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        try:
            e = str(e)
            return handle_error({'description': e[e.find(':')+2:], 'code': int(e[:3])}), int(e[:3])
        except Exception as e:
            return handle_error({'description': "Error inesperado en el servidor", 'code': 500}), 500
        
        
@mod.route('/reports/<int:id_report>', methods=['DELETE'])
def delete_report(id_report):
    try:
        result = query(SQL_STRINGS.GET_REPORT_BY_ID, {'id_report': id_report}, True)
        if result["status"] == "NOT_FOUND":
            return handle_error({'description': 'No se encontró el reporte con id {}'.format(id_report),'code': 404}), 404
        elif result["status"] != "OK":
            return handle_error({'description': 'No se pudo obtener el reporte','code': 500}), 500
        
        # * Validating null values
        response = sql(SQL_STRINGS.LOGIC_DELETE_REPORT, {"id_report": id_report})
        if (response["status"] != "OK"):
            return handle_error({'description': 'Error inesperado en la actualización del reporte', 'code': 500}), 500
        
        return jsonify({"status": 'OK', "data": {"message": "Se eliminó correctamente", "report_details": result["data"]}}), 200
    except Exception as e:
        print("Ha ocurrido un error en @create_report/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        try:
            e = str(e)
            return handle_error({'description': e[e.find(':')+2:], 'code': int(e[:3])}), int(e[:3])
        except Exception as e:
            return handle_error({'description': "Error inesperado en el servidor", 'code': 500}), 500
        
        
@mod.route('/reports/delete_image/<int:id_image>', methods=['PUT'])
def delete_report_image(id_image):
    try:
        result = query(SQL_STRINGS.GET_REPORT_IMAGE_BY_ID, {'id_image': id_image}, True)
        
        if result["status"] == "NOT_FOUND":
            return handle_error({'description': 'No hay resultados de reportes','code': 404}), 404
        elif result["status"] != "OK":
            return handle_error({'description': 'No se pudo obtener los resultados de reportes','code': 500}), 500
        
        reports_dict = [dict(row) for row in result["data"]]
        for report in reports_dict:
            if report["images"] is not None:
                report["images"] = report["images"].split(",")
            else:
                report["images"] = []
        return jsonify({
            'status': result["status"],
            'data': reports_dict
        }), 200
    except Exception as e:
        print("Ha ocurrido un error en @delete_report_image/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        try:
            e = str(e)
            return handle_error({'description': e[e.find(':')+2:], 'code': int(e[:3])}), int(e[:3])
        except Exception as e:
            return handle_error({'description': "Error inesperado en el servidor", 'code': 500}), 500