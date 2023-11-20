import os
from flask import Flask
from dotenv import load_dotenv
# modulo api rest
from flask_restful import Api
# modulo base de datos
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

api = Api()

db = SQLAlchemy()

jwt = JWTManager()

def create_app():

  app = Flask(__name__)

  cors = CORS(app, resources = {r'/*': {'origins': '*'} })

  # cargar variables de entorno
  load_dotenv()
  
  # configuracion base de datos
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  app.config['SQLALCHEMY_ENGINE_OPTIONS'] ={
    "pool_pre_ping": True, 
    "pool_recycle": 3600,
  }

  app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://AUTH_API_USER:auth_api_user_pass2023*@voz-ciudadana.cuhuub668g0y.us-east-2.rds.amazonaws.com:3306/VOZ_CIUDADANA_DB"

  db.init_app(app)

  # importa el init de resources

  import main.controllers as controllers

  api.add_resource(controllers.UsuarioController, '/update-first-access/<id>')

  # inicializa la api en app principal
  api.init_app(app)

  app.config['JWT_SECRET_KEY'] = "ejemplo123"
  app.config['JWT_ACCESS_TOKEN_EXPIRES'] = int(3600)

  jwt.init_app(app)

  from main.auth import routes
  app.register_blueprint(auth.routes.auth)

  return app