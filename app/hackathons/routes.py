from flask import Blueprint, render_template, request, redirect
from app.models import Hackathon, Team, Submission
from app import db
import os 
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user
from app.models import Registration

hackathon_bp = Blueprint("hackathons", __name__)


@hackathon_bp.route("/")
def index():

    hackathons = Hackathon.query.all()

    return render_template("index.html", hackathons=hackathons)


@hackathon_bp.route("/dashboard")
def dashboard():

    hackathons = Hackathon.query.all()

    total_hackathons = Hackathon.query.count()

    total_teams = Team.query.count()

    total_submissions = Submission.query.count()

    return render_template(
        "dashboard.html",
        hackathons=hackathons,
        total_hackathons=total_hackathons,
        total_teams=total_teams,
        total_submissions=total_submissions
    )


@hackathon_bp.route("/create_hackathon", methods=["GET","POST"])
def create_hackathon():

    if request.method == "POST":

        title = request.form["title"]
        description = request.form["description"]
        prize = request.form["prize"]

        file = request.files["banner"]

        filename = None

        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join("static/uploads", filename))

        hackathon = Hackathon(
            title=title,
            description=description,
            prize=prize,
            banner=filename
        )

        db.session.add(hackathon)
        db.session.commit()

        return redirect("/dashboard")

    return render_template("create_hackathon.html")

@hackathon_bp.route("/explore")
def explore():

    query = request.args.get("q")

    hackathons = Hackathon.query

    if query:
        hackathons = hackathons.filter(
            Hackathon.title.contains(query)
        )

    hackathons = hackathons.all()

    return render_template(
        "explore.html",
        hackathons=hackathons
    )
    
@hackathon_bp.route("/register_hackathon/<int:id>")
@login_required
def register_hackathon(id):

    registration = Registration(
        user_id=current_user.id,
        hackathon_id=id
    )

    db.session.add(registration)
    db.session.commit()

    return redirect(f"/hackathon/{id}")