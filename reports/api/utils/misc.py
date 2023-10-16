import bcrypt
from flask import jsonify
from cerberus import Validator
import jwt, datetime, string, random
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt, create_access_token
from api import api

# Schemas validate
def val_req_data(data, schema): # validate request data
    v = Validator(schema)
    if not v.validate(data):
        return {"message": v.errors}
    return None


def gen_jwt(user_id, user_role):
    try:
        payload = {
            "user_id": user_id,
            "user_role": user_role,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=(24))
        }
        return create_access_token(identity=payload, expires_delta=datetime.timedelta(hours=(24)))
    except Exception as e:
        print("Ha ocurrido un error en @misc.gen_jwt/: {} en la linea {}".format(e, e.__traceback__.tb_lineno))
        
        
def verify_jwt_token(token):
    try:
        decoded_token = jwt.decode(token, api.config['JWT_SECRET_KEY'], algorithms=['HS256'])
        return decoded_token
    except jwt.exceptions.ExpiredSignatureError:
        return 'Sesión expirada. Vuelve a iniciar sesión.'
    except jwt.exceptions.InvalidTokenError:
        return 'Tolen no válido. Vuelve a iniciar sesión.'
    
    
def hash_password(password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8')

def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def handle_error(e):
    status_message = "ERROR"
    if isinstance(e, dict):
        error_message = e.get('description', 'Error desconocido')
        error_code = e.get('code', 500)
        error_details = e.get('details', None)
        if error_code == 404:
            status_message = "NOT_FOUND"
        elif error_code == 400:
            status_message = "BAD_REQUEST"
        elif error_code == 401:
            status_message = "UNAUTHORIZED"
        elif error_code == 403:
            status_message = "FORBIDDEN"
        elif error_code == 405:
            status_message = "METHOD_NOT_ALLOWED"
        elif error_code == 406:
            status_message = "NOT_ACCEPTABLE"
        elif error_code == 408:
            status_message = "REQUEST_TIMEOUT"
        elif error_code == 500:
            status_message = "INTERNAL_SERVER_ERROR"
        elif error_code == 501:
            status_message = "NOT_IMPLEMENTED"
        elif error_code == 502:
            status_message = "BAD_GATEWAY"
        elif error_code == 503:
            status_message = "SERVICE_UNAVAILABLE"
        elif error_code == 504:
            status_message = "GATEWAY_TIMEOUT"
        elif error_code == 505:
            status_message = "HTTP_VERSION_NOT_SUPPORTED"
        else:
            status_message = "ERROR"
        e_message = f'{error_code} {status_message.capitalize()}: {error_message}'
        return jsonify(error=str(e_message), status=status_message, error_code=error_code, details = error_details)
    else:
        raise Exception('No se recibió un error válido')
    
    
def get_dict_coords(string_coords): 
    coords_array = string_coords.split(', ')
    coords_dict = {}
    coords_dict['lat'] = coords_array[0][4:]
    coords_dict['lng'] = coords_array[1][4:]
    return coords_dict