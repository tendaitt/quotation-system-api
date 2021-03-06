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


def test_add_new_product_when_none_exists(test_client, test_db):
    new_product = {
        'name': 'Tables',
        'description': '10 seater',
        'quantity': 5,
        'price': 500
    }

    response = test_client.post(
        '/v1/inventory',
        json=new_product,
        content_type='application/json'
    )

    assert response.status_code == 201
    assert response.data == b'New product successfully created'


def test_cannot_add_duplicate_product(test_client, test_db):
    new_product = {
        'name': 'Tables',
        'description': '10 seater',
        'quantity': 5,
        'price': 500
    }

    test_client.post(
        '/v1/inventory',
        json=new_product,
        content_type='application/json'
    )

    response = test_client.post(
        '/v1/inventory',
        json=new_product,
        content_type='application/json'
    )

    assert response.status_code == 409
    assert response.data == b'Product, Tables, already exists'


def test_cannot_add_product_with_existing_name(test_client, test_db):
    new_product = {
        'name': 'Tables',
        'description': '10 seater',
        'quantity': 5,
        'price': 500
    }

    test_client.post(
        '/v1/inventory',
        json=new_product,
        content_type='application/json'
    )

    new_product_2 = {
        'name': 'Tables',
        'description': '5 seater',
        'quantity': 1,
        'price': 50
    }

    response = test_client.post(
        '/v1/inventory',
        json=new_product_2,
        content_type='application/json'
    )

    assert response.status_code == 409
    assert response.data == b'A product with that name already exists'


def test_delete_existing_product(test_client, test_db):
    new_product = {
        'name': 'Tables',
        'description': '10 seater',
        'quantity': 5,
        'price': 500
    }

    test_client.post(
        '/v1/inventory',
        json=new_product,
        content_type='application/json'
    )

    response = test_client.delete('/v1/inventory/1')

    assert response.status_code == 200
    assert response.data == b'Product successfully deleted'


def test_delete_non_existent_product(test_client, test_db):
    response = test_client.delete('/v1/inventory/1')

    assert response.status_code == 404
    assert response.data == b'Product not found'


def test_get_all_products(test_client, test_db):
    response = test_client.get('/v1/inventory/all')

    assert response.status_code == 200


def test_get_existing_product_by_id(test_client, test_db):
    new_product = {
        'name': 'Tables',
        'description': '10 seater',
        'quantity': 5,
        'price': 500
    }

    test_client.post(
        '/v1/inventory',
        json=new_product,
        content_type='application/json'
    )

    response = test_client.get('/v1/inventory/1')

    assert response.status_code == 200


def test_get_non_existent_product_by_id(test_client, test_db):
    response = test_client.get('/v1/inventory/1')

    assert response.status_code == 404
    assert response.data == b'Product not found'


def test_update_existing_product(test_client, test_db):
    new_product = {
        'name': 'Tables',
        'description': '10 seater',
        'quantity': 5,
        'price': 500
    }

    test_client.post(
        '/v1/inventory',
        json=new_product,
        content_type='application/json'
    )

    updated_product = {
        'id': 1,
        'name': 'Tables',
        'description': '10 seater',
        'quantity': 1,
        'price': 25
    }

    response = test_client.put(
        '/v1/inventory',
        json=updated_product,
        content_type='application/json'
    )

    assert response.status_code == 201
    assert response.data == b'Product information was updated'


def test_cannot_update_non_existent_product(test_client, test_db):
    non_existent_product = {
        'name': 'Tables',
        'description': '10 seater',
        'quantity': 1,
        'price': 25
    }

    response = test_client.put(
        '/v1/inventory',
        json=non_existent_product,
        content_type='application/json'
    )

    assert response.status_code == 404
    assert response.data == b'Product not found'
