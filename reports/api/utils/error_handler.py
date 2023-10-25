from flask import Blueprint, jsonify
from flask_cors import CORS

errors = Blueprint('errors', __name__)
CORS(errors)

@errors.app_errorhandler(400)
def bad_request(error):
    return handle_error({
        "description": "La solicitud no pudo ser procesada debido a un error del cliente...",
        "code": 400,
        "details": str(error)
    })

@errors.app_errorhandler(401)
def unauthorized(error):
    return handle_error({
        "description": "No está autorizado para acceder a este recurso...",
        "code": 401,
        "details": str(error)
    })

@errors.app_errorhandler(403)
def forbidden(error):
    return handle_error({
        "description": "No tiene permisos para acceder a este recurso...",
        "code": 403,
        "details": str(error)
    })

@errors.app_errorhandler(404)
def not_found(error):
    return handle_error({
        "description": "No se encontró el recurso solicitado...",
        "code": 404,
        "details": str(error)
    })

@errors.app_errorhandler(500)
def server_error(error):
    return handle_error({
        "description": "Se produjo un error interno en el servidor...",
        "code": 500,
        "details": str(error)
    })

@errors.app_errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "No se encontró el recurso solicitado...",
        "status": "NOT_FOUND",
        "error_code": 404,
        "details": None
    })
    
@errors.app_errorhandler(405)
def method_not_allowed(error):
    return handle_error({
        "description": "Método no permitido...",
        "code": 405,
        "details": str(error)
    })

@errors.app_errorhandler(406)
def not_acceptable(error):
    return handle_error({
        "description": "El servidor no puede responder con la representación solicitada...",
        "code": 406,
        "details": str(error)
    })

@errors.app_errorhandler(408)
def request_timeout(error):
    return handle_error({
        "description": "La solicitud tardó demasiado...",
        "code": 408,
        "details": str(error)
    })

@errors.app_errorhandler(501)
def not_implemented(error):
    return handle_error({
        "description": "La funcionalidad solicitada no está implementada...",
        "code": 501,
        "details": str(error)
    })

@errors.app_errorhandler(502)
def bad_gateway(error):
    return handle_error({
        "description": "El servidor recibió una respuesta inválida de un servidor ascendente...",
        "code": 502,
        "details": str(error)
    })

@errors.app_errorhandler(503)
def service_unavailable(error):
    return handle_error({
        "description": "El servidor no está listo para manejar la solicitud...",
        "code": 503,
        "details": str(error)
    })

@errors.app_errorhandler(504)
def gateway_timeout(error):
    return handle_error({
        "description": "La puerta de enlace ha agotado el tiempo de espera...",
        "code": 504,
        "details": str(error)
    })

@errors.app_errorhandler(505)
def http_version_not_supported(error):
    return handle_error({
        "description": "El servidor no soporta la versión del protocolo HTTP utilizada en la solicitud...",
        "code": 505,
        "details": str(error)
    })

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
        e_message = f'{error_code} {status_message.cerrorstalize()}: {error_message}'
        return jsonify(error=str(e_message), status=status_message, error_code=error_code, details = error_details)
    else:
        raise Exception('No se recibió un error válido')