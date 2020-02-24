from connexion import request
from flask import make_response, abort, jsonify

from src import db
from src.models import Quote, QuoteItem, Transaction


def create_quote(body):  # noqa: E501
    if request.is_json:
        customer_id = body.get('customer_id')
        date = body.get('date')
        description = body.get('description')

        new_quote = Quote(
            customer_id=customer_id,
            date=date,
            description=description
        )

        db.session.add(new_quote)
        db.session.commit()

        line_items = body.get('quote_items')

        for item in line_items:
            new_quote_item = QuoteItem(
                product_id=item.get('product_id'),
                product_quantity=item.get('product_quantity'),
                product_price=item.get('product_price'),
                quote_id=new_quote.id
            )
            db.session.add(new_quote_item)

        amount = 0

        new_transaction = Transaction(
            customer_id=customer_id,
            quote_id=new_quote.id,
            date=date,
            amount=amount
        )

        db.session.add(new_transaction)
        db.session.commit()

        return make_response('New quote was successfully created', 201)


def delete_quote(quoteID):  # noqa: E501
    """Deletes a quote

     # noqa: E501

    :param quoteID: ID of quote to be deleted
    :type quoteID: int

    :rtype: None
    """
    return 'do some magic!'


def get_all_quotes():  # noqa: E501
    results = db.session.query(Quote).order_by(Quote.date.asc())
    all_quotes = []

    for result in results:
        all_quote_items = []

        items = db.session.query(QuoteItem)\
            .filter_by(quote_id=result.id)

        for item in items:
            data = {
                'id': item.id,
                'product_id': item.product_id,
                'product_quantity': item.product_quantity,
                'product_price': item.product_price,
                'quote_id': item.quote_id
            }
            all_quote_items.append(data)

        quote = {
            'id': result.id,
            'customer_id': result.customer_id,
            'descriptioin': result.description,
            'date': result.date,
            'quote_items': all_quote_items
        }

        all_quotes.append(quote)

    return make_response(jsonify(items=all_quotes), 200)


def get_quote_by_id(quoteID):  # noqa: E501
    """Find quote by ID

    Returns a single quote # noqa: E501

    :param quoteID: ID of the quote to return
    :type quoteID: int

    :rtype: Quote
    """
    return 'do some magic!'
