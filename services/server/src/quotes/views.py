from connexion import request
from flask import make_response, jsonify

from src import db
from src.models import Quote, QuoteItem, Transaction


def create_quote(body):  # noqa: E501
    if request.is_json:
        customer_id = body.get('customer_id')
        date = body.get('date')
        description = body.get('description')
        total = body.get('total')

        new_quote = Quote(
            customer_id=customer_id,
            date=date,
            description=description,
            total=total
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

        new_transaction = Transaction(
            customer_id=customer_id,
            quote_id=new_quote.id,
            date=date,
            total=total
        )

        db.session.add(new_transaction)
        db.session.commit()

        return make_response('New quote was successfully created', 201)


def delete_quote(quoteID):
    quote = db.session.query(Quote).filter_by(id=quoteID)

    if quote.one_or_none() is None:
        return make_response('Quote not found', 404)

    quote_id = quote.first().id
    quote_items = db.session.query(QuoteItem).filter_by(quote_id=quote_id)
    transaction = db.session.query(Transaction).filter_by(quote_id=quote_id)

    quote_items.delete()
    transaction.delete()
    quote.delete()

    db.session.commit()

    return make_response('Quote successfully deleted', 200)


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
            'description': result.description,
            'date': result.date,
            'quote_items': all_quote_items
        }

        all_quotes.append(quote)

    return make_response(jsonify(items=all_quotes), 200)


def get_quote_by_id(quoteID):
    result = db.session.query(Quote).filter_by(id=quoteID).first()

    if result is None:
        return make_response('Quote not found', 404)

    all_quote_items = []

    items = db.session.query(QuoteItem).filter_by(quote_id=result.id)

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
        'description': result.description,
        'date': result.date,
        'quote_items': all_quote_items
    }

    return make_response(quote, 200)
