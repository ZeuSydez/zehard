# project/users/views.py


### imports ###
from flask import Blueprint, render_template, \
    redirect, url_for, request, session
from project import bcrypt, db
from project.methods import validate
from models import User


### create users_bp ###
users_bp = Blueprint("users", __name__)


##############
### routes ###
##############

@users_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if True:
            username = request.form.get("username")
            email = request.form.get("email")
            password = request.form.get("password")
            user = User(username=username,
                        email=email, 
                        password=bcrypt.generate_password_hash(password)
                        )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("users.login"))
    return render_template("register.html")

@users_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if True:
            user = User.query.filter_by(username=request.form.get("username")).first()
            if user is not None and bcrypt.check_password_hash(user.password, request.form.get("password")):
                session["login"] = True
                print("Login başarili")
    return render_template("login.html")