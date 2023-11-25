def serialize_exception(exception):
    """Serializa una excepción a un formato JSONizable."""
    return {
        "type": exception.__class__.__name__,
        "message": str(exception),
        "args": exception.args
    }

