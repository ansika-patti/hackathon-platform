from app import db
from flask_login import UserMixin


class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    role = db.Column(db.String(20))


class Hackathon(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200))
    description = db.Column(db.Text)
    prize = db.Column(db.String(100))

    banner = db.Column(db.String(200))


class Team(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))

    hackathon_id = db.Column(db.Integer)

    leader_id = db.Column(db.Integer)


class TeamMember(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    team_id = db.Column(db.Integer)

    user_email = db.Column(db.String(100))


class Submission(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    team_id = db.Column(db.Integer)

    project_title = db.Column(db.String(200))

    github_link = db.Column(db.String(200))

    description = db.Column(db.Text)

    score = db.Column(db.Integer, default=0)
    
class Registration(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer)

    hackathon_id = db.Column(db.Integer)