from main.repositories import UsuarioRepository

usuario_repository = UsuarioRepository()

class UsuarioService():

    def updateFirstAccess(self, id):

        usuario = usuario_repository.getId(id)
        usuario.first_access = False
        updateUsuario = usuario_repository.update(usuario)

        return updateUsuario