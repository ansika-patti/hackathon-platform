from flask import Blueprint, render_template, request, redirect
from flask_login import current_user, login_required
from app.models import Team, TeamMember
from app import db

team_bp = Blueprint("teams", __name__)


@team_bp.route("/create_team/<int:hackathon_id>", methods=["GET", "POST"])
@login_required
def create_team(hackathon_id):

    if request.method == "POST":

        name = request.form["name"]

        team = Team(
            name=name,
            hackathon_id=hackathon_id,
            leader_id=current_user.id
        )

        db.session.add(team)
        db.session.commit()

        return redirect(f"/team/{team.id}")

    return render_template("create_team.html")


@team_bp.route("/team/<int:id>")
@login_required
def team_dashboard(id):

    team = Team.query.get(id)

    members = TeamMember.query.filter_by(team_id=id).all()

    return render_template(
        "team_dashboard.html",
        team=team,
        members=members
    )


@team_bp.route("/invite/<int:team_id>", methods=["POST"])
@login_required
def invite_member(team_id):

    email = request.form["email"]

    member = TeamMember(
        team_id=team_id,
        user_email=email
    )

    db.session.add(member)
    db.session.commit()

    return redirect(f"/team/{team_id}")