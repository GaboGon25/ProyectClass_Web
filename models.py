from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    #Campos de la tabla/modelo
    id= db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email_user = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)

    #formatear datos, imprimirlos
    def __repr__(self):
        return f"username: {self.username} Email: {self.email_user}"