from src import db


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
