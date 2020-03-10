import pytest

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

from src import create_app
from src.database import db
from src.authentication import bcrypt, login_manager
from src.models import Customer, Product

TEST_DB = "test"


@pytest.fixture(scope='function')
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
def test_bcrypt(test_app):
    with test_app.app_context():
        bcrypt.init_app(test_app)
        yield bcrypt


@pytest.fixture(scope='function')
def test_login_manager(test_app):
    with test_app.app_context():
        login_manager.init_app(test_app)
        yield login_manager


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


@pytest.fixture(scope='function')
def quote_dependencies(test_db):
    new_customer = Customer(
        first_name='John',
        last_name='Doe',
        email='john@doe.com',
        phone_number='(000) 000-0000'
    )

    new_product = Product(
        name='Tables',
        description='10 seater',
        quantity=5,
        price=500
    )

    test_db.session.add(new_customer)
    test_db.session.add(new_product)
    test_db.session.commit()
