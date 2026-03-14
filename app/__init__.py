from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()

login_manager.login_view = "auth.login"


def create_app():

    app = Flask(__name__,
                template_folder="../templates",
                static_folder="../static")

    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Import blueprints
    from app.auth.routes import auth_bp
    from app.hackathons.routes import hackathon_bp
    from app.teams.routes import team_bp
    from app.submissions.routes import submission_bp
    from app.judges.routes import judge_bp

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(hackathon_bp)
    app.register_blueprint(team_bp)
    app.register_blueprint(submission_bp)
    app.register_blueprint(judge_bp)

    with app.app_context():
        db.create_all()

    return app