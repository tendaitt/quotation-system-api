from connexion import request
from flask import make_response, jsonify
from sqlalchemy.exc import IntegrityError

from src import login_manager, bcrypt, db
from src.models import User


@login_manager.user_loader
def load_user(user_id):
    return User.get_id(user_id)


def login(username, password):
    return 'do some magic!'


def logout():
    return 'do some magic!'


def register(body):
    if request.is_json:
        username = body.get('username')
        email = body.get('email')
        password = bcrypt.generate_password_hash(body.get('password'))
        image_url = body.get('image_url')

        new_user = User(
            username=username,
            email=email,
            password=password,
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
