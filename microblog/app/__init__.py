import os
from flask import Flask
from flask_login import LoginManager
from flask_openid import OpenID
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import basedir


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)


login = LoginManager()
login.login_view = 'login'
login.init_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))
from app import views, models