# from .. import db

# class ImagenReporte(db.Model):
#     __tablename__ = "ImagenReporte"
#     id = db.Column(db.Integer, primary_key = True)
#     imagenReporte = db.Column(db.String(200), nullable = False)
#     reporteCiudadano = db.relationship("ReporteCiudadano", back_populates="imagenReporte")

#     def __repr__(self) -> str:
#         return f'{self.imagenReporte}'
