from src.models import Quote, QuoteItem, Transaction


def test_add_new_quote_to_database(test_db, quote_dependencies):
    new_quote = Quote(
        customer_id=1,
        date='01/01/2020',
        description='New quote',
        total=2500
    )

    test_db.session.add(new_quote)
    test_db.session.commit()

    quote = Quote.query\
        .filter(Quote.customer_id == 1)\
        .filter(Quote.date == '01/01/2020')\
        .filter(Quote.description == 'New quote')\
        .filter(Quote.total == 2500)\
        .one_or_none()

    assert quote is not None


def test_add_new_quote_item_to_database(test_db, quote_dependencies):
    new_quote = Quote(
        customer_id=1,
        date='01/01/2020',
        description='New quote',
        total=2500
    )

    test_db.session.add(new_quote)
    test_db.session.commit()

    new_quote_item = QuoteItem(
        product_id=1,
        product_quantity=5,
        product_price=500,
        quote_id=1
    )

    test_db.session.add(new_quote_item)
    test_db.session.commit()

    quote_item = QuoteItem.query\
        .filter(QuoteItem.product_id == 1)\
        .filter(QuoteItem.product_quantity == 5)\
        .filter(QuoteItem.product_price == 500)\
        .filter(QuoteItem.quote_id == 1)\
        .one_or_none()

    assert quote_item is not None


def test_add_new_transaction_to_database(test_db, quote_dependencies):
    new_quote = Quote(
        customer_id=1,
        date='01/01/2020',
        description='New quote',
        total=2500
    )

    new_quote_item = QuoteItem(
        product_id=1,
        product_quantity=5,
        product_price=500,
        quote_id=1
    )

    test_db.session.add(new_quote)
    test_db.session.add(new_quote_item)
    test_db.session.commit()

    new_transaction = Transaction(
        customer_id=1,
        quote_id=new_quote.id,
        date=new_quote.date,
        total=new_quote.total
    )

    test_db.session.add(new_transaction)
    test_db.session.commit()

    transaction = Transaction.query\
        .filter(Transaction.customer_id == 1)\
        .filter(Transaction.quote_id == 1)\
        .filter(Transaction.date == new_quote.date)\
        .filter(Transaction.total == new_quote.total)\
        .one_or_none()

    assert transaction is not None


def test_add_new_quote(test_client, test_db, quote_dependencies):
    new_quote = {
        "customer_id": 1,
        "date": '01/01/2020',
        "description": "New quote",
        "total": 2500,
        "quote_items": [
            {
                "product_id": 1,
                "product_price": 500,
                "product_quantity": 5
            }
        ]
    }

    response = test_client.post(
        'v1/quote',
        json=new_quote,
        content_type='application/json'
    )

    assert response.status_code == 201
    assert response.data == b'New quote was successfully created'


def test_delete_existing_quote(test_client, test_db, quote_dependencies):
    new_quote = {
        "customer_id": 1,
        "date": '01/01/2020',
        "description": "New quote",
        "total": 2500,
        "quote_items": [
            {
                "product_id": 1,
                "product_price": 500,
                "product_quantity": 5
            }
        ]
    }

    test_client.post(
        'v1/quote',
        json=new_quote,
        content_type='application/json'
    )

    response = test_client.delete('/v1/quote/1')

    assert response.status_code == 200
    assert response.data == b'Quote successfully deleted'


def test_delete_non_existent_quote(test_client, test_db, quote_dependencies):
    response = test_client.delete('/v1/quote/1')

    assert response.status_code == 404
    assert response.data == b'Quote not found'


def test_get_all_quotes(test_client, test_db, quote_dependencies):
    response = test_client.get('v1/quote/all')

    assert response.status_code == 200


def test_get_existing_quote_by_id(test_client, test_db, quote_dependencies):
    new_quote = {
        "customer_id": 1,
        "date": '01/01/2020',
        "description": "New quote",
        "total": 2500,
        "quote_items": [
            {
                "product_id": 1,
                "product_price": 500,
                "product_quantity": 5
            }
        ]
    }

    test_client.post(
        'v1/quote',
        json=new_quote,
        content_type='application/json'
    )

    response = test_client.get('/v1/quote/1')

    assert response.status_code == 200


def test_get_non_existent_quote_by_id(test_client, test_db, quote_dependencies):
    pass
