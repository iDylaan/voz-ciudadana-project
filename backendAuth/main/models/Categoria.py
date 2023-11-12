# from .. import db

# class Categoria(db.Model):
#     __tablename__ = 'Categoria'
#     id = db.Column(db.Integer, primary_key = True)
#     nombreCategoria = db.Column(db.String(50), nullable = False)
#     reporteCiudadano = db.relationship("ReporteCiudadano", back_populates="categoria")

#     def __repr__(self) -> str:
#         return f'{self.nombreCategoria}'
