import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from project.model import User


@app.route("/")
@app.route("/hello")
def hello_world():
    return "Hello, World!"
