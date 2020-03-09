import os
import connexion

from src.database import db
from src.authentication import login_manager, bcrypt


def create_app():

    app = connexion.App(__name__, specification_dir='../')
    app.add_api('swagger.yml')
    application = app.app
    application.config.from_object(os.environ['APP_SETTINGS'])

    return application


def init_bcrypt(app):
    bcrypt.init_app(app)


def init_db(app):
    db.init_app(app)


def init_login_manager(app):
    login_manager.init_app(app)


app = create_app()
init_db(app)
init_login_manager(app)
