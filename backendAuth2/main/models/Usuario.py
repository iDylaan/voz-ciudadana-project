from .. import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    __tablename__ = 'USERS'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(255), nullable = False, unique=True)
    username = db.Column(db.String(255), nullable = False)
    password = db.Column(db.String(255), nullable = False)
    is_admin = db.Column(db.Boolean, nullable = False, default=False)
    is_active = db.Column(db.Boolean, nullable = False, default=True)
    profile_picture = db.Column(db.Integer, nullable = False, default=1)
    profile_banner = db.Column(db.Integer, nullable = False, default=1)
    first_access = db.Column(db.Boolean, nullable = False, default=True)

    def __repr__(self) -> str:
        return f'{self.email}'

    @property
    def plain_password(self):
        raise AttributeError('La contraseña no se puede leer')

    @plain_password.setter
    def plain_password(self, password):
        self.password = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password, password)

    def to_json(self):
        usuario_json = {
            "email": self.email,
            "nombre": self.username,
            "is_admin": self.is_admin,
            "is_active": self.is_active
        }
        return usuario_json
    
    @staticmethod
    def from_json(usuario_json):
        email = usuario_json.get("email")
        username = usuario_json.get("username")
        password = usuario_json.get("password")
        is_active = usuario_json.get("is_active")
        is_admin = usuario_json.get("is_admin")

        return Usuario(
            email = email,
            username = username,
            is_active = is_active,
            plain_password = password,
            is_admin = is_admin
        )