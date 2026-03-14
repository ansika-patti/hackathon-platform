from flask import Blueprint, render_template, request, redirect
from flask_login import login_required
from app.models import Submission
from app import db

submission_bp = Blueprint("submissions", __name__)


@submission_bp.route("/submit/<int:team_id>", methods=["GET", "POST"])
@login_required
def submit_project(team_id):

    if request.method == "POST":

        title = request.form["title"]
        github = request.form["github"]
        description = request.form["description"]

        submission = Submission(
            team_id=team_id,
            project_title=title,
            github_link=github,
            description=description
        )

        db.session.add(submission)
        db.session.commit()

        return redirect("/leaderboard")

    return render_template("submission.html")