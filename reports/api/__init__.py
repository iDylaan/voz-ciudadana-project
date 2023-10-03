from flask import Flask, render_template, send_from_directory
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from .api_config import Config
from flask_cors import CORS

# Cargar variables de entorno desde .env
load_dotenv('.env')
### Cargar api ###
api = Flask(__name__)
### Configuracion de la api ###
api.config.from_object(Config)
### JWT Config ###
jwt = JWTManager(api)

### Activación de CORS ###
CORS(api) # TODO: Configurar para acceso al servidor del cliente

### API ROUTES ###
from .reports.routes import mod as mod_reports

### BP ###
api.register_blueprint(mod_reports)