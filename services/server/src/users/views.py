from src import login_manager
from src.models import User


@login_manager.user_loader
def load_user(user_id):
    return User.get_id(user_id)


def login(username, password):
    return 'do some magic!'


def logout():
    return 'do some magic!'


def new_user(body):
    return 'do some magic!'
