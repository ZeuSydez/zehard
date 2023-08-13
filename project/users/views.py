# project/users/views.py


### imports ###
from flask import Blueprint, render_template, \
    redirect, url_for, request, session
from project import bcrypt, db, mail, app, log
from models import User
from functools import wraps
from flask_mail import Message
import random as rd


### create users_bp ###
users_bp = Blueprint("users", __name__)


### Helper Functions ###
def send_email(subject, recipients, text_body, html_body):
    sender = app.config['MAIL_USERNAME']  # Gönderen e-posta adresi, app.config'ten alınıyor
    msg = Message(subject=subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)


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
            # log.log(f"username: {username}", level=log.CRITICAL)
            # log.log(f"email: {email}", level=log.CRITICAL)
            # log.log(f"password: {password}", level=log.CRITICAL)
            # log.log("", level=log.INFO, separator="****************************************")
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("users.login"))
    return render_template("register.html")

@users_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username and password:
            # log.log(f"username: {username}", level=log.CRITICAL)
            # log.log(f"password: {password}", level=log.CRITICAL)
            # log.log("", level=log.INFO, separator="****************************************")
            user = User.query.filter_by(username=username).first()
            if user is not None and bcrypt.check_password_hash(user.password, password):
                session["logged_in"] = True
                session["user_id"] = user.user_id
                return redirect(url_for("minecraft.minecraft"))
    return render_template("login.html")

@users_bp.route("/logout/", methods=["GET", "POST"])
def logout():
    session.pop("logged_in")
    session.pop("user_id")
    return redirect(url_for("users.login"))

@users_bp.route("/forgot_password", methods=["GET", "POST"])
def forgot_password():
    if request.method == "GET":
        code = "".join(str(rd.randint(0, 9)) for _ in range(6))
        session["verification_code"] = code
        print("verification_code", session["verification_code"])

    if request.method == "POST":
        code1 = request.form.get("code1")
        code2 = request.form.get("code2")
        code3 = request.form.get("code3")
        code4 = request.form.get("code4")
        code5 = request.form.get("code5")
        code6 = request.form.get("code6")
        input_code = code1 + code2 + code3 + code4 + code5 + code6
        print("input_code", input_code)
        
        if input_code == session["verification_code"]:
            return render_template("forgot_password.html", verify=True)

    return render_template("forgot_password.html")

@users_bp.route("/myaccount")
def myaccount():
    return render_template("myaccount.html")
