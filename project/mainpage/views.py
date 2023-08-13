# project/mainpage/views.py


### imports ###
from flask import Blueprint, redirect, render_template, \
    url_for


### create mainpage_bp ###
mainpage_bp = Blueprint("mainpage", __name__)


###############
### routest ###
###############

@mainpage_bp.route("/")
def mainpage():
    return redirect(url_for("minecraft.minecraft"))

@mainpage_bp.route("/color")
def color():
    return render_template("mainpage/color.html")