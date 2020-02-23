from src import db


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    image_url = db.Column(db.String, unique=True, nullable=False)

    def __init__(self, name=None, email=None, image_url=None):
        self.name = name
        self.email = email
        self.image_url = image_url

    def __repr__(self):
        return '<User {0}>'.format(self.name)


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


class Quote(db.Model):

    __tablename__ = 'quotes'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String, nullable=False)
    customer_id = db.Column(
        db.Integer,
        db.ForeignKey('customers.id'),
        nullable=False
    )

    quote_items = db.relationship('QuoteItem', backref='quotes', lazy=True)
    transactions = db.relationship('Transaction', backref='quotes', lazy=True)

    def __init__(self, date=None, description=None, customer_id=None):
        self.date = date
        self.description = description
        self.customer_id = customer_id


class QuoteItem(db.Model):

    __tablename__ = 'quote_items'

    id = db.Column(db.Integer, primary_key=True)
    product_quantity = db.Column(db.Integer, nullable=False)
    product_price = db.Column(db.Integer, nullable=False)
    product_id = db.Column(
        db.Integer,
        db.ForeignKey('products.id'),
        nullable=False
    )
    quote_id = db.Column(
        db.Integer,
        db.ForeignKey('quotes.id'),
        nullable=False
    )

    def __init__(self, product_quantity=None, product_price=None,
                 product_id=None, quote_id=None):

        self.product_quantity = product_quantity
        self.product_price = product_price
        self.product_id = product_id
        self.quote_id = quote_id


class Transaction(db.Model):

    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    customer_id = db.Column(
        db.Integer,
        db.ForeignKey('customers.id'),
        nullable=False
    )
    quote_id = db.Column(
        db.Integer,
        db.ForeignKey('quotes.id'),
        nullable=False
    )

    def __init__(self, date=None, amount=None,
                 customer_id=None, quote_id=None):

        self.date = date
        self.amount = amount
        self.customer_id = customer_id
        self.quote_id = quote_id
