def test_add_new_customer_to_database():
    pass


def test_add_new_customer_when_none_exists(test_client, test_db):
    new_customer = {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john@doe.com',
        'phone_number': '(000)000-0000'
    }

    response = test_client.post(
        '/v1/customer',
        json=new_customer,
        content_type='application/json'
    )

    assert response.status_code == 201
    assert response.data == b'New customer was succesfully created'


def test_cannont_add_duplicate_customer():
    pass


def test_cannot_add_customer_with_existing_email():
    pass


def test_cannot_add_customer_with_existing_phone_number():
    pass


def test_delete_customer():
    pass


def test_get_all_customers():
    pass


def test_get_customer_by_id():
    pass


def test_update_customer():
    pass
