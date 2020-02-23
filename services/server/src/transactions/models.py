from src import db


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
