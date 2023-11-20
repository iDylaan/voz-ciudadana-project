from .. import db
from main.models import UsuarioModel

class UsuarioRepository():

    __modelo = UsuarioModel

    @property
    def modelo(self):
        return self.__modelo
    
    def getId(self, id):
        usuario = db.session.query(self.modelo).get(id)
        if usuario is None:
            raise Exception('No existe el usuario')
        return usuario
        
    def update(self, usuario):
        db.session.add(usuario)
        db.session.commit()
        return usuario
