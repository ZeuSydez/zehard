# project/users/views.py


### imports ###
from flask import Blueprint, render_template, \
    redirect, url_for, request, session
from project import bcrypt, db
from models import User
from functools import wraps


### create users_bp ###
users_bp = Blueprint("users", __name__)


##############
### routes ###
##############

@users_bp.route("/register/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm = request.form.get("confirm")
        if username and email and password and confirm and password == confirm:
            user = User(username=username,
                        email=email, 
                        password=bcrypt.generate_password_hash(password)
                        )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("users.login"))
    return render_template("users/register.html")

@users_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form.get("username") and request.form.get("password"):
            user = User.query.filter_by(username=request.form.get("username")).first()
            if user is not None and bcrypt.check_password_hash(user.password, request.form.get("password")):
                session["logged_in"] = True
                session["user_id"] = user.user_id
                return redirect(url_for("minecraft.minecraft"))
    return render_template("users/login.html")

@users_bp.route("/logout/", methods=["GET", "POST"])
def logout():
    session.pop("logged_in")
    session.pop("user_id")
    return redirect(url_for("users.login"))