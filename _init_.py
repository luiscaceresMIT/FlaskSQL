

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key='shouldbesecret'
app.config['SQLALCHEMY DATA BASE URL'] = 'Sqlite:///data.db'
app.config['SQLALCHEMY TRACK MODIFICATIONS'] = False

db.init_app(app)

login.init_app (app)
login.login_view = 'login'

@app.before_first_request


