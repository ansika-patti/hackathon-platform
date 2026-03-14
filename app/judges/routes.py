from flask import Blueprint, render_template, request, redirect
from app.models import Submission
from app import db

judge_bp = Blueprint("judges", __name__)


@judge_bp.route("/leaderboard")
def leaderboard():

    submissions = Submission.query.order_by(
        Submission.score.desc()
    ).all()

    return render_template(
        "leaderboard.html",
        submissions=submissions
    )


@judge_bp.route("/score/<int:id>", methods=["POST"])
def score_submission(id):

    submission = Submission.query.get(id)

    score = int(request.form["score"])

    submission.score = score

    db.session.commit()

    return redirect("/leaderboard")