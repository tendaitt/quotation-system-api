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
    """Get all quotes

    Returns all quotes # noqa: E501


    :rtype: List[Quote]
    """
    return 'do some magic!'


def get_quote_by_id(quoteID):  # noqa: E501
    """Find quote by ID

    Returns a single quote # noqa: E501

    :param quoteID: ID of the quote to return
    :type quoteID: int

    :rtype: Quote
    """
    return 'do some magic!'
