from project import db


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    image_url = db.Column(db.String, unique=True, nullable=False)

    def __init__(self, name=None, email=None, image_url=None):
        self.name = name
        self.email = email
        self.image_url = image_url

    def __repr__(self):
        return '<User {0}>'.format(self.name)
