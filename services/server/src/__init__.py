import os
import connexion

from src.database import db


def create_app():

    app = connexion.App(__name__, specification_dir='../')
    app.add_api('swagger.yml')
    application = app.app
    application.config.from_object(os.environ['APP_SETTINGS'])

    return application


def init_db(app):
    db.init_app(app)


app = create_app()
init_db(app)
