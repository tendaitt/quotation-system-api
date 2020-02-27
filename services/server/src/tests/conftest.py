import os
import pytest
import csv
import psycopg2

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

from src import create_app
from src.database import db

basedir = os.path.abspath(os.path.dirname(__file__))

TEST_DB = "test"


@pytest.fixture(scope='module')
def test_app():
    app = create_app()
    with app.app_context():
        yield app


@pytest.fixture(scope='function')
def test_client(test_app):
    with test_app.app_context():
        testing_client = test_app.test_client()
        yield testing_client


@pytest.fixture(scope='function')
def test_db(test_app):
    engine = create_engine('postgresql://localhost/' + TEST_DB)

    if not database_exists(engine.url):
        create_database(engine.url)

    with test_app.app_context():

        db.init_app(test_app)
        db.create_all()

        yield db

    db.drop_all()
