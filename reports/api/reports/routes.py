from flask import Blueprint, jsonify, request
from .sql_strings import Sql_Strings as SQL_STRINGS
from api.utils.misc import val_req_data
from flask_jwt_extended import jwt_required, get_jwt_identity

mod = Blueprint('reports', __name__)

@mod.route('/reports', methods=['GET'])
def get_reports():
    return jsonify({"message": "OK on reports API"})