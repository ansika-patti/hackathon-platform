from flask import Blueprint, render_template, request, redirect
from flask_login import login_user, logout_user
from app.models import User
from app import db

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        user = User(name=name,email=email,password=password,role="participant")

        db.session.add(user)
        db.session.commit()

        return redirect("/login")

    return render_template("register.html")


@auth_bp.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email,password=password).first()

        if user:
            login_user(user)
            return redirect("/dashboard")

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():

    logout_user()

    return redirect("/")

from flask_login import login_required, current_user
from app.models import Team, Submission


@auth_bp.route("/profile")
@login_required
def profile():

    teams = Team.query.filter_by(
        leader_id=current_user.id
    ).all()

    submissions = Submission.query.all()

    return render_template(
        "profile.html",
        user=current_user,
        teams=teams,
        submissions=submissions
    )