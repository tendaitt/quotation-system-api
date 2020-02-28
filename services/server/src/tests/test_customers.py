from src.models import Customer


def test_add_new_customer_to_database(test_db):
    new_customer = Customer(
        first_name='John',
        last_name='Doe',
        email='john@doe.com',
        phone_number='(000) 000-0000'
    )

    test_db.session.add(new_customer)
    test_db.session.commit()

    customer = Customer.query\
        .filter(Customer.first_name == 'John')\
        .filter(Customer.last_name == 'Doe')\
        .filter(Customer.email == 'john@doe.com')\
        .filter(Customer.phone_number == '(000) 000-0000')\
        .one_or_none()

    assert customer is not None


def test_add_new_customer_when_none_exists(test_client, test_db):
    new_customer = {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john@doe.com',
        'phone_number': '(000) 000-0000'
    }

    response = test_client.post(
        '/v1/customer',
        json=new_customer,
        content_type='application/json'
    )

    assert response.status_code == 201
    assert response.data == b'New customer was successfully created'


def test_cannot_add_duplicate_customer(test_client, test_db):
    new_customer = {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john@doe.com',
        'phone_number': '(000) 000-0000'
    }

    test_client.post(
        '/v1/customer',
        json=new_customer,
        content_type='application/json'
    )

    response = test_client.post(
        '/v1/customer',
        json=new_customer,
        content_type='application/json'
    )

    assert response.status_code == 409
    assert response.data == b'Customer, John Doe, already exists'


def test_cannot_add_customer_with_existing_email(test_client, test_db):
    new_customer = {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john@doe.com',
        'phone_number': '(000) 000-0000'
    }

    test_client.post(
        '/v1/customer',
        json=new_customer,
        content_type='application/json'
    )

    new_customer_2 = {
        'first_name': 'Jane',
        'last_name': 'Doe',
        'email': 'john@doe.com',
        'phone_number': '(123) 456-7890'
    }

    response = test_client.post(
        '/v1/customer',
        json=new_customer_2,
        content_type='application/json'
    )

    assert response.status_code == 409
    assert response.data == b'That email/phone number already exists'


def test_cannot_add_customer_with_existing_phone_number(test_client, test_db):
    new_customer = {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john@doe.com',
        'phone_number': '(000) 000-0000'
    }

    test_client.post(
        '/v1/customer',
        json=new_customer,
        content_type='application/json'
    )

    new_customer_2 = {
        'first_name': 'Jane',
        'last_name': 'Doe',
        'email': 'jane@doe.com',
        'phone_number': '(000) 000-0000'
    }

    response = test_client.post(
        '/v1/customer',
        json=new_customer_2,
        content_type='application/json'
    )

    assert response.status_code == 409
    assert response.data == b'That email/phone number already exists'


def test_delete_existing_customer(test_client, test_db):
    new_customer = {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john@doe.com',
        'phone_number': '(000) 000-0000'
    }

    test_client.post(
        '/v1/customer',
        json=new_customer,
        content_type='application/json'
    )

    response = test_client.delete('/v1/customer/1')

    assert response.status_code == 200
    assert response.data == b'Customer successfully deleted'


def test_delete_non_existent_customer(test_client, test_db):
    response = test_client.delete('/v1/customer/1')

    assert response.status_code == 404
    assert response.data == b'Customer not found'


def test_get_all_customers(test_client, test_db):
    response = test_client.get('/v1/customer/all')

    assert response.status_code == 200


def test_get_existing_customer_by_id(test_client, test_db):
    new_customer = {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john@doe.com',
        'phone_number': '(000) 000-0000'
    }

    test_client.post(
        '/v1/customer',
        json=new_customer,
        content_type='application/json'
    )

    response = test_client.get('/v1/customer/1')

    assert response.status_code == 200


def test_get_non_existent_customer_by_id(test_client, test_db):
    response = test_client.get('/v1/customer/1')

    assert response.status_code == 404
    assert response.data == b'Customer not found'


def test_update_customer():
    pass
