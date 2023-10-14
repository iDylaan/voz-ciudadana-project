report_schema = {
    "title": {
        "type": "string",
        "required": True
    },
    "description": {
        "type": "string",
        "required": False
    },
    "user_id": {
        "type": "integer",
        "required": True
    },
    "category_id": {
        "type": "integer",
        "required": True
    },
    "status_id": {
        "type": "integer",
        "required": True
    },
    "images": {
        "type": "list",
        "required": False,
        "schema": {
            "type": "string",
            'regex': r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        }
    },
    "updated_at": {
        "type": "datetime",
        "required": False
    }
}

report_update_schema = {
    "title": {
        "type": "string",
        "required": True
    },
    "description": {
        "type": "string",
        "required": True
    },
    "category_id": {
        "type": "integer",
        "required": True
    }
}

url_image_schema = {
    "url_image": {
        "type": "string",
        'regex': r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    }
}

id_user_schema = {
    "id_user": {
        "type": "integer",
        "required": True
    }
}