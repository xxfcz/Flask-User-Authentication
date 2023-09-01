from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

login_manager = LoginManager()
bcrypt = Bcrypt()
db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
