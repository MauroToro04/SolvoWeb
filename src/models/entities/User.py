from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import UserMixin


class User(UserMixin):

    def __init__(self,id,correo_solvo,contrasena,id_solvo=0,nombres="",apellidos="",estado=0,id_supervisor=0) -> None:
        self.id=id
        self.id_solvo=id_solvo
        self.nombres=nombres
        self.apellidos=apellidos
        self.correo_solvo=correo_solvo
        self.estado=estado
        self.id_supervisor=id_supervisor
        self.contrasena=contrasena
        

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)
    def __repr__(self):
       return "<id: " + str(self.id) + "; id_solvo = " + str(self.id_solvo) + "; nombres = " + str(self.nombres)  + "; apellidos = " + str(self.apellidos) + "; correo = " + str(self.correo_solvo) + "; estado = " + str(self.estado) + "; id_supervisor = " + str(self.id_supervisor) +">"
    
    