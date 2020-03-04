from src.models import Quote, QuoteItem, Transaction, Customer


def test_add_new_quote_to_database(test_db):
    new_customer = Customer(
        first_name='John',
        last_name='Doe',
        email='john@doe.com',
        phone_number='(000) 000-0000'
    )

    test_db.session.add(new_customer)
    test_db.session.commit()

    new_quote = Quote(
        customer_id=1,
        date='01/01/2020',
        description='New quote'
    )

    test_db.session.add(new_quote)
    test_db.session.commit()

    quote = Quote.query\
        .filter(Quote.customer_id == 1)\
        .filter(Quote.date == '01/01/2020')\
        .filter(Quote.description == 'New quote')\
        .one_or_none()

    assert quote is not None


def test_add_new_quote_item_to_database(test_db):
    pass


def test_add_new_transaction_to_database(test_db):
    pass


def test_add_new_quote():
    pass


def test_delete_quote():
    pass


def test_get_all_quotes():
    pass


def test_get_quote_by_id():
    pass
