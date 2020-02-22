from src import db


class Product(db.Model):

    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)

    quote_items = db.relationship('QuoteItem', backref='products', lazy=True)

    def __init__(self, name=None, description=None, quantity=None, price=None):

        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price
