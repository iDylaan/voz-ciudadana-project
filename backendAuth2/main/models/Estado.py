# from .. import db

# class Estado(db.Model):
#     __tablename__ = 'Estado'
#     id = db.Column(db.Integer, primary_key = True)
#     nombreEstado = db.Column(db.String(30), nullable = False)
#     reporteCiudadano = db.relationship("ReporteCiudadano", back_populates="estado")

#     def __repr__(self) -> str:
#         return f'{self.nombreEstado}'
