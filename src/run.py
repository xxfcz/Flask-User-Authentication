from src.accounts.models import User
from src.core.views import core_bp
from src.accounts.views import accounts_bp
from decouple import config
from flask import Flask, render_template

from src.exts import login_manager, bcrypt, db, migrate, mail


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(config("APP_SETTINGS"))

    login_manager.init_app(app)
    bcrypt.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    # Registering blueprints

    app.register_blueprint(accounts_bp)
    app.register_blueprint(core_bp)

    login_manager.login_view = "accounts.login"
    login_manager.login_message_category = "danger"


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()


app = create_app()


########################
#### error handlers ####
########################


@app.errorhandler(401)
def unauthorized_page(error):
    return render_template("errors/401.html"), 401


@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"), 404


@app.errorhandler(500)
def server_error_page(error):
    return render_template("errors/500.html"), 500
