from src.models import Product


def test_add_new_product_to_database(test_db):
    new_product = Product(
        name='Tables',
        description='10 seater',
        quantity=5,
        price=500
    )

    test_db.session.add(new_product)
    test_db.session.commit()

    product = Product.query\
        .filter(Product.name == 'Tables')\
        .filter(Product.description == '10 seater')\
        .filter(Product.quantity == 5)\
        .filter(Product.price == 500)\
        .one_or_none()

    assert product is not None


def test_add_new_product_when_none_exists():
    pass


def test_add_new_duplicate_customer():
    pass


def test_add_product_with_existing_name():
    pass


def test_delete_product():
    pass


def test_get_all_products():
    pass


def test_get_product_by_id():
    pass


def test_update_product():
    pass
