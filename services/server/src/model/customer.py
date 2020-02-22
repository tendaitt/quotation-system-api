from src import db


class Customer(db.Model):

    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String, nullable=False)

    quotes = db.relationship('Quote', backref='customers', lazy=True)
    transactions = db.relationship(
        'Transaction',
        backref='customers',
        lazy=True
    )

    def __init__(self, first_name=None, last_name=None,
                 email=None, phone_number=None):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
