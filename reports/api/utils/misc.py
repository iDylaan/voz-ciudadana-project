import bcrypt
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