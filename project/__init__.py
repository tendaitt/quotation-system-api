import os
import connexion

from flask_sqlalchemy import SQLAlchemy

app = connexion.App(__name__, specification_dir='../')
app.add_api('server/swagger.yml')
application = app.app
application.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(application)

from project.model import User


@app.route("/")
@app.route("/hello")
def hello_world():
    return "Hello, World!"
