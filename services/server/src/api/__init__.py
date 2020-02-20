from flask import Blueprint

api_blueprint = Blueprint('api', __name__)


def add_customer(body):  # noqa: E501
    """Add a new customer

     # noqa: E501

    :param body: Customer that needs to be added
    :type body: dict | bytes

    :rtype: None
    """
    return 'do some magic!'


def delete_customer(customerID):  # noqa: E501
    """Deletes a customer

     # noqa: E501

    :param customerID: Customer ID to delete
    :type customerID: int

    :rtype: None
    """
    return 'do some magic!'


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


def add_product(body):  # noqa: E501
    """Add a new product

     # noqa: E501

    :param body: Product that needs to be added
    :type body: dict | bytes

    :rtype: None
    """
    return 'do some magic!'


def delete_product(productID):  # noqa: E501
    """Deletes a product

     # noqa: E501

    :param productID: ID of product to be deleted
    :type productID: int

    :rtype: None
    """
    return 'do some magic!'


def get_all_products():  # noqa: E501
    """Get all products

    Returns all products # noqa: E501


    :rtype: List[Product]
    """
    return 'do some magic!'


def get_product_by_id(productID):  # noqa: E501
    """Find product by ID

    Returns a single product # noqa: E501

    :param productID: ID of product to return
    :type productID: int

    :rtype: Product
    """
    return 'do some magic!'


def update_product(body):  # noqa: E501
    """Update an existing product

     # noqa: E501

    :param body: product that needs to be updated
    :type body: dict | bytes

    :rtype: None
    """
    return 'do some magic!'
