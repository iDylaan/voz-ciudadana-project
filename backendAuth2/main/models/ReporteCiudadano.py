# from .. import db
# import datetime as dt
# import pytz

# zoneMexico = pytz.timezone('America/Mexico_City')

# class ReporteCiudadano(db.Model):
#     __tablename__ = 'ReporteCiudadano'
#     id = db.Column(db.Integer, primary_key = True)
#     titulo = db.Column(db.String(100), nullable = False)
#     descripcion = db.Column(db.String(350), default =lambda: dt.datetime.now(zoneMexico), nullable = False)
#     fechaCreacion = db.Column(db.DateTime, nullable = False)
#     ubicacion = db.Column(db.String(250), nullable = False)
#     ultimaActualizacion = db.Column(db.String(350), default =lambda: dt.datetime.now(zoneMexico), nullable = False)
#     solved_request_count = db.Column(db.Integer, nullable = False, default = 0)
#     confirmation_request_count = db.Column(db.Integer, nullable = False, default = 0)

#     usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
#     usuario = db.relationship("Usuario", back_populates="reporteCiudadanos")

#     estado_id = db.Column(db.Integer, db.ForeignKey('estado.id'))
#     estado = db.relationship("Estado", back_populates="reporteCiudadanos")

#     categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'))
#     categoria = db.relationship("Categoria", back_populates="reporteCiudadano")

#     imagen_reporte_id = db.Column(db.Integer, db.ForeignKey('imagen_reporte.id'))
#     imagen_reporte = db.relationship("ImagenReporte", back_populates="reporteCiudadano")





#     def __repr__(self) -> str:
#         return f'{self.email}'


