## OBTENER TODOS LOS REPORTES
endpoint: `/reports`
method: `GET`
body: `NA`

## OBTENER REPORTE POR ID
endpoint: `/reports/<report_id>`
method: `GET`
body: `NA`

## CREAR UN NUEVO REPORTE
endpoint: `/reports`
method: `POST`
body: 
```bash
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
        'regex': r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+' # REGEX para URL
    }
},
"updated_at": {
    "type": "datetime",
    "required": False
},
"coords": {
    "type": "dict", # diccionario (python)
    "schema": {
        "lat": {"type": "float", "required": True},  # Rango de latitudes válidas
        "lng": {"type": "float", "required": True}  # Rango de longitudes válidas
    },
    "required": True
}
```

## ACTUALIZAR REPORTE POR SU ID
endpoint: `/reports/<report_id>`
method: `PUT`
body: 
```bash
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
},
"user_id": {
    "type": "integer",
    "required": True
}
```

## ELIMINAR REPORTE POR SU ID (baja logica)
endpoint: `/reports/<report_id>`
method: `DELETE`
body: `NA`

## AGREGAR IMAGEN A UN REPORTE POR SU ID
endpoint: `/reports/add_image/<report_id>`
method: `POST`
body: 
```bash
url_image: {
    "type": "string",
    "regex": r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+' # REGEX para URL
}
```

## ELIMINAR IMAGEN A SU ID (baja logica)
endpoint: `/reports/delete_image/<image_id>`
method: `DELETE`
body: `NA`

## CAMBIAR EL ESTADO DE CONFIRMACION DE UN REPORTE POR SU ID
endpoint: `/reports/toggle_confirm/<report_id>`
method: `POST`
body: 
```bash
id_user: {
    "type": "integer",
    "required": True
}
```

## CAMBIAR EL ESTADO DE CONFIRMACION DE ATENCION DE UN REPORTE POR SU ID
endpoint: `/reports/toggle_fix_confirm/<report_id>`
method: `POST`
body: 
```bash
id_user: {
    "type": "integer",
    "required": True
}
```