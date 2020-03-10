from src.models import User


def test_users_can_be_added_to_database(test_db, test_bcrypt):
    new_user = User(
        username='johndoe',
        email='john@doe.com',
        password=test_bcrypt.generate_password_hash('johndoe'),
        image_url='https://dummyimage.com/629x296'
    )

    test_db.session.add(new_user)
    test_db.session.commit()

    users = test_db.session.query(User).all()

    for user in users:
        user.username

    assert user.username == 'johndoe'


def test_users_cannot_login_unless_registered(test_client, test_db):
    response = test_client.get(
        '/v1/user/login?username=johndoe&password=johndoe',
    )

    assert response.status_code == 400
    assert response.data == b'Invalid username/password supplied'


def test_users_can_login():
    pass


def test_user_cannot_login_with_invalid_information():
    pass


def test_user_can_register():
    pass


def test_user_cannot_register_with_existing_credentials():
    pass


def test_logged_in_users_can_logout():
    pass


def test_not_logged_in_users_cannot_logout():
    pass


def test_new_user(test_client, test_bcrypt, test_db):

    new_user = {
        'username': 'johndoe',
        'email': 'john@doe.com',
        'password': 'johndoe',
        'image_url': 'https://dummyimage.com/629x296'
    }

    response = test_client.post(
        '/v1/user',
        json=new_user,
        content_type='application/json'
    )

    assert response.status_code == 201
