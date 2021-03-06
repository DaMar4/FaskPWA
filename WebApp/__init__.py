from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
app = Flask(__name__)

app.config.from_object("configuration.DevelopmentConfig")

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "blue_login.login"
login_manager.login_message=""

from WebApp.modules.iniciar.login_user import blue_login
from WebApp.modules.home.index import index
from WebApp.modules.home.CRUD import crud
from WebApp.modules.home.catalog import alta_catalogo

app.register_blueprint(index)
app.register_blueprint(blue_login)
app.register_blueprint(crud)
app.register_blueprint(alta_catalogo)
db.create_all()
