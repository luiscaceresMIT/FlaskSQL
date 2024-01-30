from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
login = LoginManager(app)

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    pw_hash = db.Column(db.String(200))

    def set_pw(self, pwd):
        self.pw_hash = generate_password_hash(pwd)

    def check_pw(self, password):
        return check_password_hash(self.pw_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

with app.app_context():
    db.create_all()
