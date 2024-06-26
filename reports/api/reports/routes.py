import datetime
from flask import Blueprint, jsonify, request, json
from .sql_strings import Sql_Strings as SQL_STRINGS
from api.utils.misc import val_req_data, handle_error, get_dict_coords
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import CORS
from api.config.conf_mysql import query, sql
from .schemas import report_schema, report_update_schema, url_image_schema, id_user_schema

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
        result_reports = []
        for report in reports_dict:
            result_report = {}
            result_report["id"] = report["id"]
            result_report["title"] = report["report_title"]
            result_report["description"] = report["report_description"]
            result_report["category"] = {
                "id": report["category_id"],
                "category_name": report["category_name"],
                "icon_name": report["icon_name"],
            }
            result_report["status"] = {
                "id": report["status_id"],
                "status_name": report["status_name"]
            }
            result_report["created_at"] = report["creation_dt"]
            result_report["last_update"] = report["last_updated_dt"]
            result_report["user"] = {
                "id": report["user_id"],
                "username": report["username"]
            } 
            result_report["coords"] = get_dict_coords(report["coords"])
            result_report["images"] = []
            if report["images"]:
                images_dict = [json.loads(segment) for segment in str(report["images"]).split('|')]
                for image in images_dict:
                    if image["id"] is not None and image["image"] is not None:
                        result_report["images"].append(image)
            result_reports.append(result_report)
        return jsonify({
            'status': result["status"],
            'data': result_reports
        }), 200
    except Exception as e:
        print("Ha ocurrido un error en @get_reports/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        try:
            e = str(e)
            return handle_error({'description': e[e.find(':')+2:], 'code': int(e[:3])}), int(e[:3])
        except Exception as e:
            return handle_error({'description': "Error inesperado en el servidor", 'code': 500}), 500


@mod.route('/user_reports/<int:id_user>', methods=['GET'])
@jwt_required()
def get_user_reports(id_user):
    try:
        result_user = query(SQL_STRINGS.GET_USER_BY_ID, {'id_user': id_user}, True)
        if result_user["status"] == "NOT_FOUND":
            return handle_error({'description': 'No se encontró el usuario con id {}'.format(id_user),'code': 404}), 404
        elif result_user["status"]!= "OK":
            return handle_error({'description': 'No se pudo obtener el usuario con id {}'.format(id_user),'code': 500}), 500
        
        result = query(SQL_STRINGS.GET_USER_REPORTS, {'id_user': id_user})
        if result["status"] == "NOT_FOUND":
            return jsonify({"success": True, "data": []}), 200
        elif result["status"]!= "OK":
            return handle_error({'description': 'No se pudo obtener los reportes para el usuario con id {}'.format(id_user),'code': 500}), 500
        
        reports_dict = [dict(row) for row in result["data"]]
        result_reports = []
        for report in reports_dict:
            result_report = {}
            result_report["id"] = report["id"]
            result_report["title"] = report["report_title"]
            result_report["description"] = report["report_description"]
            result_report["category"] = {
                "id": report["category_id"],
                "category_name": report["category_name"],
                "icon_name": report["icon_name"],
            }
            result_report["status"] = {
                "id": report["status_id"],
                "status_name": report["status_name"]
            }
            result_report["created_at"] = report["creation_dt"]
            result_report["last_update"] = report["last_updated_dt"]
            result_report["user"] = {
                "id": report["user_id"],
                "username": report["username"]
            } 
            result_report["coords"] = get_dict_coords(report["coords"])
            result_report["images"] = []
            if report["images"]:
                images_dict = [json.loads(segment) for segment in str(report["images"]).split('|')]
                for image in images_dict:
                    if image["id"] is not None and image["image"] is not None:
                        result_report["images"].append(image)
            result_reports.append(result_report)
        return jsonify({
            'status': result["status"],
            'data': result_reports
        }), 200
    except Exception as e:
        print("Ha ocurrido un error en @get_user_reports/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
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
        
        result_report = {}
        result_report["id"] =result["data"]["id"]
        result_report["title"] =result["data"]["report_title"]
        result_report["description"] =result["data"]["report_description"]
        result_report["category"] = {
            "id":result["data"]["category_id"],
            "category_name":result["data"]["category_name"]
        }
        result_report["status"] = {
            "id":result["data"]["status_id"],
            "status_name":result["data"]["status_name"]
        }
        result_report["created_at"] = result["data"]["creation_dt"]
        result_report["last_update"] = result["data"]["last_updated_dt"]
        result_report["user"] = {
            "id":result["data"]["user_id"],
            "username":result["data"]["username"]
        } 
        result_report["coords"] = get_dict_coords(result["data"]["coords"])
        result_report["images"] = []
        if result["data"]["images"]:
            images_dict = [json.loads(segment) for segment in str(result["data"]["images"]).split('|')]
            for image in images_dict:
                if image["id"] is not None and image["image"] is not None:
                    result_report["images"].append(image)
        return jsonify({
            'status': result["status"],
            'data': result_report
        }), 200
    except Exception as e:
        print("Ha ocurrido un error en @get_report/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        try:
            e = str(e)
            return handle_error({'description': e[e.find(':')+2:], 'code': int(e[:3])}), int(e[:3])
        except Exception as e:
            return handle_error({'description': "Error inesperado en el servidor", 'code': 500}), 500
    
    
    
@mod.route('/reports', methods=['POST'])
@jwt_required()
def create_report():
    try:
        data = request.get_json()

        # * Validating null values
        title = data.get("title", None)
        description = data.get("description", None)
        user_id = data.get("user_id", None)
        category_id = data.get("category_id", None),
        coords = data.get("coords", None)
        if not title \
        or not user_id \
        or not coords \
        or not category_id:
            missing_data = []
            if title is None:
                missing_data.append({"title": "Titulo del reporte"})
            if user_id is None:
                missing_data.append({"user_id": "ID del usuario que realiza el reporte"})
            if category_id is None:
                missing_data.append({"category_id": "ID de la categoria del reporte"})
            if coords is None:
                missing_data.append({"coords": "Faltan las coordenadas del reporte"})
            return handle_error({'description': 'Error inesperado en el servidor','code': 400, 'details': {'missing_data': missing_data}}), 400
        
        new_report = {
            "title": title,
            "description": description,
            "user_id": int(user_id),
            "category_id": int(category_id[0]),
            "status_id": 1,
            "images": [],
            "coords": coords
        }
        images = data.get("images", None)
        if images is not None:
            for image in images:
                new_report["images"].append(image)
        errors = val_req_data(new_report, report_schema)
        if errors:
            return handle_error({'description': 'Error en la validación de la petición','code': 400, 'details': errors}), 400
        
        result = query(SQL_STRINGS.GET_USER_BY_ID, {'id_user': user_id}, True)
        if result["status"] == "NOT_FOUND":
            return handle_error({'description': 'No se encontró el usuario con id {}'.format(user_id),'code': 404}), 404
        elif result["status"]!= "OK":
            return handle_error({'description': 'No se pudo obtener el usuario','code': 500}), 500
        
        result = query(SQL_STRINGS.GET_CATEGORY_BY_ID, {'category_id': category_id}, True)
        if result["status"] == "NOT_FOUND":
            return handle_error({'description': 'No se encontró la categoria con id {}'.format(category_id),'code': 404}), 404
        elif result["status"]!= "OK":
            return handle_error({'description': 'No se pudo obtener la categoria','code': 500}), 500
        
        new_report['coords'] = 'lat:{}, lng:{}'.format(new_report['coords']['lat'], new_report['coords']['lng'])
        
        result = sql(SQL_STRINGS.INSERT_REPORT, {
            "report_title": new_report['title'],
            "report_description": new_report['description'],
             "user_id": new_report['user_id'],
            "category_id": new_report['category_id'],
            "status_id": new_report['status_id'],
            "coords": new_report['coords'],
        })
        if (result["status"] != "OK"):
            return handle_error({'description': 'Error inesperado en el registro del reporte', 'code': 500}), 500
        
        if len(new_report['images']) > 0:
            values_insrt = ''
            for index, image in enumerate(new_report['images']):
                values_insrt += '(\'{}\', {}, 1), '.format(image, result['last_insert_id']) \
                    if index < len(new_report['images']) - 1 \
                    else '(\'{}\', {}, 1)'.format(image, result['last_insert_id'])
            new_report['id'] = result['last_insert_id']
            
            result = sql(SQL_STRINGS.INSERT_REPORT_IMAGES.format(values_insrt))
            if (result["status"] != "OK"):
                return handle_error({'description': 'Error inesperado en el registro de las imagenes del reporte', 'code': 500}), 500
        
        new_report['coords'] = get_dict_coords(new_report['coords'])
        return jsonify({"status": 'OK', "data": new_report}), 200
    except Exception as e:
        print("Ha ocurrido un error en @create_report/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        try:
            e = str(e)
            return handle_error({'description': e[e.find(':')+2:], 'code': int(e[:3])}), int(e[:3])
        except Exception as e:
            return handle_error({'description': "Error inesperado en el servidor", 'code': 500}), 500



@mod.route('/reports/<int:id_report>', methods=['PUT'])
@jwt_required()
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
        coords = data.get("coords", None)
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
            "coords": old_report["coords"] if coords is None else coords
        }
        
        errors = val_req_data(new_report, report_update_schema)
        if errors:
            return handle_error({'description': 'Error en la validación de la petición','code': 400, 'details': errors}), 400
        new_report['coords'] = 'lat:{}, lng:{}'.format(new_report['coords']['lat'], new_report['coords']['lng'])
        result = sql(SQL_STRINGS.UPDATE_REPORT, {
            "report_title": new_report['title'],
            "report_description": new_report['description'],
            "category_id": new_report['category_id'],
            "coords": new_report['coords'],
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
@jwt_required()
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
        
        
@mod.route('/reports/delete_image/<int:id_image>', methods=['DELETE'])
@jwt_required()
def delete_report_image(id_image):
    try:
        result = query(SQL_STRINGS.GET_REPORT_IMAGE_BY_ID, {'id_image': id_image}, True)
        
        if result["status"] == "NOT_FOUND":
            return handle_error({'description': 'No se encontró la imagen con id {}'.format(id_image),'code': 404}), 404
        elif result["status"] != "OK":
            return handle_error({'description': 'No se pudo obtener la imagen a eliminar','code': 500}), 500
        
        response = sql(SQL_STRINGS.LOGIC_DELETE_REPORT_IMAGE, {"id_image": id_image})
        if (response["status"] != "OK"):
            return handle_error({'description': 'Error inesperado al eliminar la imagen', 'code': 500}), 500
        result["data"]["is_active"] = 0
        return jsonify({
            'status': response["status"],
            'data': {"message": "Se eliminó correctamente la imagen", "report_image_details": result["data"]}
        }), 200
    except Exception as e:
        print("Ha ocurrido un error en @delete_report_image/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        try:
            e = str(e)
            return handle_error({'description': e[e.find(':')+2:], 'code': int(e[:3])}), int(e[:3])
        except Exception as e:
            return handle_error({'description': "Error inesperado en el servidor", 'code': 500}), 500
        
        
        
@mod.route('/reports/add_image/<int:id_report>', methods=['POST'])
@jwt_required()
def add_report_image(id_report):
    try:
        result = query(SQL_STRINGS.GET_REPORT_BY_ID, {'id_report': id_report}, True)
        if result["status"] == "NOT_FOUND":
            return handle_error({'description': 'No se encontró el reporte con id {}'.format(id_report),'code': 404}), 404
        elif result["status"] != "OK":
            return handle_error({'description': 'No se pudo obtener el reporte','code': 500}), 500
        
        data = request.get_json()
        report_url_image = data.get('url_image', None)
        if report_url_image is None:
            return handle_error({'description': 'Error en la validación de la petición','code': 400, 'details': {'missing_data': ['url_image']}}), 400

        errors = val_req_data({"url_image": report_url_image}, url_image_schema)
        if errors:
            return handle_error({'description': 'Error en la validación de la petición','code': 400, 'details': errors}), 400
        
        response = sql(SQL_STRINGS.INSERT_REPORT_IMAGE, {"id_report": id_report, "url_image": report_url_image})
        if (response["status"] != "OK"):
            return handle_error({'description': 'Error inesperado al eliminar la imagen', 'code': 500}), 500
        
        result = query(SQL_STRINGS.GET_IMAGE_BY_ID, {'id_image': response["last_insert_id"]}, True)
        
        return jsonify({
            'status': response["status"],
            'data': {"message": "Se agregó correctamente la imagen", "report_image_details": result["data"]}
        }), 200
    except Exception as e:
        print("Ha ocurrido un error en @add_report_image/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        try:
            e = str(e)
            return handle_error({'description': e[e.find(':')+2:], 'code': int(e[:3])}), int(e[:3])
        except Exception as e:
            return handle_error({'description': "Error inesperado en el servidor", 'code': 500}), 500
        

@mod.route('/reports/toggle_confirm/<int:id_report>', methods=['POST'])
@jwt_required()
def toggle_confirm(id_report):
    try:
        data = request.get_json()
        id_user = data.get('id_user', None)
        if id_user is None:
            return handle_error({'description': 'Error en la validación de la petición','code': 400, 'details': {'missing_data': ['id_user']}}), 400
        errors = val_req_data({"id_user": id_user}, id_user_schema)
        if errors:
            return handle_error({'description': 'Error en la validación de la petición','code': 400, 'details': errors}), 400
        
        report_result = query(SQL_STRINGS.GET_REPORT_BY_ID, {'id_report': id_report}, True)
        if report_result["status"] == "NOT_FOUND":
            return handle_error({'description': 'No se encontró el reporte con id {}'.format(id_report),'code': 404}), 404
        elif report_result["status"] != "OK":
            return handle_error({'description': 'No se pudo obtener el reporte','code': 500}), 500
        
        user_result = query(SQL_STRINGS.GET_USER_BY_ID, {'id_user': id_user}, True)
        if user_result["status"] == "NOT_FOUND":
            return handle_error({'description': 'No se encontró al usuario con id {}'.format(id_user),'code': 404}), 404
        elif user_result["status"] != "OK":
            return handle_error({'description': 'No se pudo consultar al usuario','code': 500}), 500

        # Obtener si ya existe el registro de la confirmación
        id_user = int(id_user)
        confirmation_result = query(SQL_STRINGS.GET_CONFIRMATION_BY_REPORT_AND_USER, {"id_report": id_report, "id_user": id_user}, True)
        confirmation_exists = None
        if confirmation_result["status"] == "NOT_FOUND":
            confirmation_exists = False
            confirmation_result["data"] = {"unconfirmed": 0}
        elif confirmation_result["status"] == "OK":
            confirmation_exists = True
            
        user_result["data"]["unconfirmed"] = int(confirmation_result["data"]["unconfirmed"])
        if confirmation_exists:
            if bool(user_result["data"]["unconfirmed"]):
                response = sql(SQL_STRINGS.SET_CONFIRM_REPORT, {"id_report": id_report, "id_user": id_user})
                if (response["status"] != "OK"):
                    return handle_error({'description': 'Error inesperado al registrar la confirmación', 'code': 500}), 500
                user_result["data"]["unconfirmed"] = 0 if bool(user_result["data"]["unconfirmed"]) else 1
                return jsonify({
                    'status': response["status"],
                    'data': {"message": "Se confirmó el reporte correctamente", "report_confirmation_details": user_result["data"]}
                }), 200
            else:
                response = sql(SQL_STRINGS.UNCONFIRM_REPORT, {"id_report": id_report, "id_user": id_user})
                if (response["status"] != "OK"):
                    return handle_error({'description': 'Error inesperado al registrar la desconfirmación', 'code': 500}), 500
                user_result["data"]["unconfirmed"] = 0 if bool(user_result["data"]["unconfirmed"]) else 1
                return jsonify({
                    'status': response["status"],
                    'data': {"message": "Se desconfirmó el reporte correctamente", "report_confirmation_details": user_result["data"]}
                }), 200
        else:
            response = sql(SQL_STRINGS.CONFIRM_REPORT, {"id_report": id_report, "id_user": id_user})
            if (response["status"] != "OK"):
                return handle_error({'description': 'Error inesperado al registrar la confirmación', 'code': 500}), 500
            return jsonify({
                'status': response["status"],
                'data': {"message": "Se confirmó el reporte correctamente", "report_confirmation_details": user_result["data"]}
            }), 200
    except Exception as e:
        print("Ha ocurrido un error en @toggle_confirm/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        try:
            e = str(e)
            return handle_error({'description': e[e.find(':')+2:], 'code': int(e[:3])}), int(e[:3])
        except Exception as e:
            return handle_error({'description': "Error inesperado en el servidor", 'code': 500}), 500



@mod.route('/reports/toggle_fix_confirm/<int:id_report>', methods=['POST'])
@jwt_required()
def toggle_fix_confirm(id_report):
    try:
        data = request.get_json()
        id_user = data.get('id_user', None)
        if id_user is None:
            return handle_error({'description': 'Error en la validación de la petición','code': 400, 'details': {'missing_data': ['id_user']}}), 400
        errors = val_req_data({"id_user": id_user}, id_user_schema)
        if errors:
            return handle_error({'description': 'Error en la validación de la petición','code': 400, 'details': errors}), 400
        
        report_result = query(SQL_STRINGS.GET_REPORT_BY_ID, {'id_report': id_report}, True)
        if report_result["status"] == "NOT_FOUND":
            return handle_error({'description': 'No se encontró el reporte con id {}'.format(id_report),'code': 404}), 404
        elif report_result["status"] != "OK":
            return handle_error({'description': 'No se pudo obtener el reporte','code': 500}), 500
        
        user_result = query(SQL_STRINGS.GET_USER_BY_ID, {'id_user': id_user}, True)
        if user_result["status"] == "NOT_FOUND":
            return handle_error({'description': 'No se encontró al usuario con id {}'.format(id_user),'code': 404}), 404
        elif user_result["status"] != "OK":
            return handle_error({'description': 'No se pudo consultar al usuario','code': 500}), 500

        # Obtener si ya existe el registro de la confirmación
        id_user = int(id_user)
        confirmation_result = query(SQL_STRINGS.GET_FIXED_CONFIRMATION_BY_REPORT_AND_USER, {"id_report": id_report, "id_user": id_user}, True)
        confirmation_exists = None
        if confirmation_result["status"] == "NOT_FOUND":
            confirmation_exists = False
            confirmation_result["data"] = {"unconfirmed": 0}
        elif confirmation_result["status"] == "OK":
            confirmation_exists = True
            
        user_result["data"]["unconfirmed"] = int(confirmation_result["data"]["unconfirmed"])
        if confirmation_exists:
            if bool(user_result["data"]["unconfirmed"]):
                response = sql(SQL_STRINGS.SET_FIXED_CONFIRM_REPORT, {"id_report": id_report, "id_user": id_user})
                if (response["status"] != "OK"):
                    return handle_error({'description': 'Error inesperado al registrar la confirmación de atendimiento', 'code': 500}), 500
                user_result["data"]["unconfirmed"] = 0 if bool(user_result["data"]["unconfirmed"]) else 1
                return jsonify({
                    'status': response["status"],
                    'data': {"message": "Se confirmó el atendimiento el reporte correctamente", "report_confirmation_details": user_result["data"]}
                }), 200
            else:
                response = sql(SQL_STRINGS.FIXED_UNCONFIRM_REPORT, {"id_report": id_report, "id_user": id_user})
                if (response["status"] != "OK"):
                    return handle_error({'description': 'Error inesperado al registrar la desconfirmación', 'code': 500}), 500
                user_result["data"]["unconfirmed"] = 0 if bool(user_result["data"]["unconfirmed"]) else 1
                return jsonify({
                    'status': response["status"],
                    'data': {"message": "Se desconfirmó el atendimiento el reporte correctamente", "report_confirmation_details": user_result["data"]}
                }), 200
        else:
            response = sql(SQL_STRINGS.FIXED_CONFIRM_REPORT, {"id_report": id_report, "id_user": id_user})
            if (response["status"] != "OK"):
                return handle_error({'description': 'Error inesperado al registrar la confirmación', 'code': 500}), 500
            return jsonify({
                'status': response["status"],
                'data': {"message": "Se confirmó el atendimiento el reporte correctamente", "report_confirmation_details": user_result["data"]}
            }), 200
    except Exception as e:
        print("Ha ocurrido un error en @toggle_fix_confirm/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        try:
            e = str(e)
            return handle_error({'description': e[e.find(':')+2:], 'code': int(e[:3])}), int(e[:3])
        except Exception as e:
            return handle_error({'description': "Error inesperado en el servidor", 'code': 500}), 500
        

@mod.route('/pending_reports', methods=['GET'])
def get_pending_reports():
    try:
        response = query(SQL_STRINGS.GET_PENDING_REPORTS)
        if (response["status"] != "OK"):
            return handle_error({'description': 'Error inesperado al registrar la confirmación', 'code': 500}), 500
        reports_dict = [dict(row) for row in response["data"]]
        
        result_reports = []
        for report in reports_dict:
            result_report = {}
            result_report["id"] = report["id"]
            result_report["title"] = report["report_title"]
            result_report["description"] = report["report_description"]
            result_report["category"] = {
                "id": report["category_id"],
                "category_name": report["category_name"]
            }
            result_report["status"] = {
                "id": report["status_id"],
                "status_name": report["status_name"]
            }
            result_report["created_at"] = report["creation_dt"]
            result_report["last_update"] = report["last_updated_dt"]
            result_report["user"] = {
                "id": report["user_id"],
                "username": report["username"]
            } 
            result_report["coords"] = get_dict_coords(report["coords"])
            result_report["images"] = []
            if report["images"]:
                images_dict = [json.loads(segment) for segment in str(report["images"]).split('|')]
                for image in images_dict:
                    if image["id"] is not None and image["image"] is not None:
                        result_report["images"].append(image)
            result_reports.append(result_report)
        return jsonify({
            "success": True,
            "data": result_reports
        })
    except Exception as e:
        print("Ha ocurrido un error en @get_pending_reports/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        try:
            e = str(e)
            return handle_error({'description': e[e.find(':')+2:], 'code': int(e[:3])}), int(e[:3])
        except Exception as e:
            return handle_error({'description': "Error inesperado en el servidor", 'code': 500}), 500
        
        
@mod.route('/activate_report/<int:id_report>', methods=['POST'])
@jwt_required()
def activate_report(id_report):
    try:
        response = sql(SQL_STRINGS.ACTIVATE_REPORT_BY_ID, {"id_report": id_report})
        if (response["status"] != "OK"):
            return handle_error({'description': 'Error inesperado al registrar la confirmación del reporte', 'code': 500}), 500
        return jsonify({
            "success": True,
            "data": {
                "message": "Se activó el reporte correctamente",
                "report_activated": True
            }
        })
    except Exception as e:
        print("Ha ocurrido un error en @activate_report/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        try:
            e = str(e)
            return handle_error({'description': e[e.find(':')+2:], 'code': int(e[:3])}), int(e[:3])
        except Exception as e:
            return handle_error({'description': "Error inesperado en el servidor", 'code': 500}), 500

@mod.route('/declinate_report/<int:id_report>', methods=['POST'])
@jwt_required()
def declinate_report(id_report):
    try:
        response = sql(SQL_STRINGS.DECLINATE_REPORT_BY_ID, {"id_report": id_report})
        if (response["status"] != "OK"):
            return handle_error({'description': 'Error inesperado al rechazar el reporte', 'code': 500}), 500
        return jsonify({
            "success": True,
            "data": {
                "message": "Se reachazó el reporte correctamente",
                "report_declinated": True
            }
        })
    except Exception as e:
        print("Ha ocurrido un error en @declinate_report/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        try:
            e = str(e)
            return handle_error({'description': e[e.find(':')+2:], 'code': int(e[:3])}), int(e[:3])
        except Exception as e:
            return handle_error({'description': "Error inesperado en el servidor", 'code': 500}), 500