# project/__init__.py


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from logger import MyLogger


app = Flask(__name__)
app.config.from_pyfile("_config.py")
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
mail = Mail(app)
log = MyLogger()

from project.users.views import users_bp
from project.minecraft.views import minecraft_bp
from project.mainpage.views import mainpage_bp


app.register_blueprint(users_bp)
app.register_blueprint(minecraft_bp)
app.register_blueprint(mainpage_bp)