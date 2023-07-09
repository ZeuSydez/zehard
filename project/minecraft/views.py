# project/minecraft/views.py


### imports ###
from flask import Blueprint, render_template, \
    redirect, url_for, session, request
from functools import wraps
from models import MCCoord
from project import db


### create minecraft.bp ###
minecraft_bp = Blueprint("minecraft", __name__)


########################
### helper functions ###
########################

def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return test(*args, **kwargs)
        else:
            return redirect(url_for("users.login"))
    return wrap

def coords():
    return db.session.query(MCCoord).order_by(MCCoord.coord_id.asc())

##############
### routes ###
##############

@minecraft_bp.route("/minecraft", methods=["GET", "POST"])
@login_required
def minecraft():
    if request.method == "POST":
        coord_name = request.form.get("coord_name")
        coord_x = request.form.get("coord_x")
        coord_y = request.form.get("coord_y")
        coord_z = request.form.get("coord_z")
        if True:
            new_coord = MCCoord(
                coord_name,
                coord_x,
                coord_y,
                coord_z,
                session["user_id"]
            )
            print(coord_name)
            print(coord_x)
            print(coord_y)
            print(coord_z)
            print(session["user_id"])
            db.session.add(new_coord)
            db.session.commit()
            return redirect(url_for("minecraft.minecraft"))
    return render_template("minecraft.html", coords=coords())


