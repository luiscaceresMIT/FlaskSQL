from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, LoginManager

login = LoginManager()
db = SQLAlchemy()

app = Flask(__name__)

# Configura la clave secreta y la URI de la base de datos
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tu_base_de_datos.db'

# Inicializa las extensiones
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'  # Especifica la vista que maneja los inicios de sesión

# Modelo de usuario
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Manejador de carga del usuario para Flask-Login
@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Asegúrate de crear las tablas en la base de datos
with app.app_context():
    db.create_all()
