from connexion import request
from flask import make_response, abort, jsonify

from src import db
from src.models import Customer


def add_customer(body):
    if request.is_json:
        first_name = body.get('first_name')
        last_name = body.get('last_name')
        email = body.get('email')
        phone_number = body.get('phone_number')

        new_customer = Customer(first_name, last_name, email, phone_number)

        existing_customer = Customer.query\
            .filter(Customer.first_name == first_name)\
            .filter(Customer.last_name == last_name)\
            .filter(Customer.email == email)\
            .filter(Customer.phone_number == phone_number)\
            .one_or_none()

        if existing_customer is None:
            db.session.add(new_customer)
            db.session.commit()
            return make_response('New customer was succesfully created', 201)
        else:
            abort(409, f'Customer, {first_name} {last_name}, already exists')


def delete_customer(customerID):
    customer = db.session.query(Customer).filter_by(id=customerID)

    if customer is None:
        abort('Customer not found', 404)

    customer.delete()
    db.session.commit()
    return make_response('Customer succesfully deleted', 200)


def get_all_customers():  # noqa: E501
    results = db.session.query(Customer)\
        .order_by(Customer.first_name.asc())
    all_customers = []

    for result in results:
        customer = {
            'id': result.id,
            'first_name': result.first_name,
            'last_name': result.last_name,
            'email': result.email,
            'phone_number': result.phone_number
        }
        all_customers.append(customer)

    return make_response(jsonify(items=all_customers), 200)


def get_customer_by_id(customerID):
    result = db.session.query(Customer).filter_by(id=customerID).first()

    if result is None:
        return 'Customer not found', 404

    customer = {
        'id': result.id,
        'first_name': result.first_name,
        'last_name': result.last_name,
        'email': result.email,
        'phone_number': result.phone_number
    }

    return make_response(customer, 200)


def update_customer(body):  # noqa: E501
    """Update an existing customer

     # noqa: E501

    :param body: Customer object to be added
    :type body: dict | bytes

    :rtype: None
    """
    return 'do some magic!'
