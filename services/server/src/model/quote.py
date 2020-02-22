from src import db


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

    quote_items = db.relationship('QuoteItems', backref='quotes', lazy=True)
    transactions = db.relationship('Transaction', backref='quotes', lazy=True)

    def __init__(self, date=None, description=None, customer_id=None):
        self.date = date
        self.description = description
        self.customer_id = customer_id
