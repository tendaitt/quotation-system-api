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


def new_user(body):  # noqa: E501
    """Register a new user

     # noqa: E501

    :param body: User that needs to be created
    :type body: dict | bytes

    :rtype: None
    """
    return 'do some magic!'


def create_quote(body):  # noqa: E501
    """Create a new quote

     # noqa: E501

    :param body: Quote that needs to be created
    :type body: dict | bytes

    :rtype: None
    """
    return 'do some magic!'


def delete_quote(quoteID):  # noqa: E501
    """Deletes a quote

     # noqa: E501

    :param quoteID: ID of quote to be deleted
    :type quoteID: int

    :rtype: None
    """
    return 'do some magic!'


def get_all_quotes():  # noqa: E501
    """Get all quotes

    Returns all quotes # noqa: E501


    :rtype: List[Quote]
    """
    return 'do some magic!'


def get_quote_by_id(quoteID):  # noqa: E501
    """Find quote by ID

    Returns a single quote # noqa: E501

    :param quoteID: ID of the quote to return
    :type quoteID: int

    :rtype: Quote
    """
    return 'do some magic!'
