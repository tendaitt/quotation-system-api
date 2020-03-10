from connexion import request
from flask import make_response
from sqlalchemy.exc import IntegrityError
from flask_login import current_user, logout_user, login_user

from src import login_manager, bcrypt, db
from src.models import User


@login_manager.user_loader
def load_user(user_id):
    return User.get_id(user_id)


def login(username, password):
    if username is not None and password is not None:
        existing_user = User.query\
            .filter_by(username=username)\
            .first()

        valid_user = existing_user is not None and bcrypt.check_password_hash(
            existing_user.password, password)

        if valid_user:
            existing_user.authenticated = True
            db.session.add(existing_user)
            db.session.commit()
            login_user(existing_user)
            return make_response('User successfully logged in', 200)
        else:
            return make_response('Invalid username/password supplied', 400)
    else:
        return make_response('Invalid username/password supplied', 400)


def logout():
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return make_response('User successfully logged out', 200)


def register(body):
    if request.is_json:
        username = body.get('username')
        email = body.get('email')
        password = bcrypt.generate_password_hash(body.get('password'))
        image_url = body.get('image_url')

        new_user = User(
            username=username,
            email=email,
            password=password.decode('utf-8'),
            image_url=image_url
        )

        existing_user = User.query\
            .filter(User.username == username)\
            .filter(User.email == email)\
            .one_or_none()

        if existing_user is None:
            try:
                db.session.add(new_user)
                db.session.commit()
                return make_response(
                    'New user was successfully created',
                    201
                )
            except IntegrityError:
                return make_response(
                    'A user with the same credentials already exists',
                    409
                )
        else:
            return make_response(
                f'User, {username}, already exists',
                409
            )
