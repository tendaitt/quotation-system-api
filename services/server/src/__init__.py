import os
import connexion

from flask_sqlalchemy import SQLAlchemy


def create_app():

    app = connexion.App(__name__, specification_dir='../')
    app.add_api('swagger.yml')
    application = app.app
    application.config.from_object(os.environ['APP_SETTINGS'])

    return application


app = create_app()

db = SQLAlchemy(app)

from src.model import User


@app.route("/")
@app.route("/hello")
def hello_world():
    return "Hello, World!"
