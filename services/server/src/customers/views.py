from connexion import request
from flask import make_response, abort

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
    """Get all customers

    Returns all customers # noqa: E501


    :rtype: List[Customer]
    """
    return 'do some magic!'


def get_customer_by_id(customerID):  # noqa: E501
    """Find customer by ID

    Returns a single customer # noqa: E501

    :param customerID: ID of customer to return
    :type customerID: int

    :rtype: Customer
    """
    return 'do some magic!'


def update_customer(body):  # noqa: E501
    """Update an existing customer

     # noqa: E501

    :param body: Customer object to be added
    :type body: dict | bytes

    :rtype: None
    """
    return 'do some magic!'
