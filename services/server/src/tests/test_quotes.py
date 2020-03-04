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


def test_add_new_quote():
    pass


def test_delete_quote():
    pass


def test_get_all_quotes():
    pass


def test_get_quote_by_id():
    pass
