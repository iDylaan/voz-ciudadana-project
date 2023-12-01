from flask import request, Blueprint
from .. import db
from main.models import UsuarioModel
from flask_jwt_extended import create_access_token
from main.auth.decorators import user_identity_lookup

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/login', methods=['POST'])
def login():
  #Buscamos al usuario en la db mediante el mail
  usuario = db.session.query(UsuarioModel).filter(UsuarioModel.email == request.get_json().get('email')).first()
  #Validamos la contraseña de ese usuario
  try:
    if usuario.validate_password(request.get_json().get("password")):
      #Generamos un nuevo token y le pasamos al usuario como identidad de es token
      access_token = create_access_token(identity=usuario)
      #Devolvemos los valores y el token

      if usuario.first_access == True:
        usuario.first_access = False
        db.session.add(usuario)
        db.session.commit()

      data = {
          'email': usuario.email,
          'nombre': usuario.username,
          'access_token': access_token,
          'status': 'ok'
      }
      return data, 200
    else:
      return {
        'message': 'Usuario o Contraseña incorrecta',
        "status": "error"
      }, 400
  except:
    db.session.rollback()
    return {
        'message': 'Error al iniciar sesion',
        "status": "error"
      }, 400
  finally:
    db.session.close()

@auth.route('/register', methods=['POST'])
def register():
  usuario = UsuarioModel.from_json(request.get_json())
  exits = db.session.query(UsuarioModel).filter(UsuarioModel.email == usuario.email).scalar() is not None
  if exits:
    return {
      "message": 'El correo ya esta en uso',
      "status": "error"
    }, 409
  else:
    try:
      db.session.add(usuario)
      db.session.commit()
      return usuario.to_json(), 200
    except:
      db.session.rollback()
      return {
        'message': 'Error al iniciar sesion',
        "status": "error"
      }, 400
    finally:
      db.session.close()