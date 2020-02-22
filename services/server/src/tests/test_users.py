import unittest
import pytest

from flask import json

from ..model.user import User


@pytest.fixture(autouse=True)
class TestUser(unittest.TestCase):
    """UserController integration test stubs"""

    def test_new_user(self, app):
        """Test case for new_user

        Register a new user
        """
        body = User()
        response = app.client.open(
            '/v1/user',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
