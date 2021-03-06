from src import db


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, unique=True, nullable=False)
    authenticated = db.Column(db.Boolean, default=False)

    def __init__(self, id=None, username=None, email=None,
                 password=None, image_url=None):

        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.image_url = image_url

    def __repr__(self):
        return '<User {0}>'.format(self.name)

    def is_active(self):
        return True

    def get_id(self):
        return self.username

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False


class Customer(db.Model):

    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String, unique=True, nullable=False)

    quotes = db.relationship('Quote', backref='customers', lazy=True)
    transactions = db.relationship(
        'Transaction',
        backref='customers',
        lazy=True
    )

    def __init__(self, id=None, first_name=None, last_name=None,
                 email=None, phone_number=None):

        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number


class Product(db.Model):

    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)

    quote_items = db.relationship('QuoteItem', backref='products', lazy=True)

    def __init__(self, id=None, name=None,
                 description=None, quantity=None, price=None):

        self.id = id
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price


class Quote(db.Model):

    __tablename__ = 'quotes'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    customer_id = db.Column(
        db.Integer,
        db.ForeignKey('customers.id'),
        nullable=False
    )

    quote_items = db.relationship('QuoteItem', backref='quotes', lazy=True)
    transactions = db.relationship('Transaction', backref='quotes', lazy=True)

    def __init__(self, id=None, date=None,
                 description=None, total=None, customer_id=None):

        self.id = id
        self.date = date
        self.description = description
        self.total = total
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

    def __init__(self, id=None, product_quantity=None, product_price=None,
                 product_id=None, quote_id=None):

        self.id = id
        self.product_quantity = product_quantity
        self.product_price = product_price
        self.product_id = product_id
        self.quote_id = quote_id


class Transaction(db.Model):

    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    total = db.Column(db.Integer, nullable=False)
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

    def __init__(self, id=None, date=None, total=None,
                 customer_id=None, quote_id=None):
        self.id = id
        self.date = date
        self.total = total
        self.customer_id = customer_id
        self.quote_id = quote_id
