import pytest

from src import create_app


@pytest.fixture(scope='module')
def test_app():
    app = create_app()
    with app.app_context():
        testing_client = app.test_client()
        yield testing_client
