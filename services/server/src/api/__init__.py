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


def add_inventory_item(body):  # noqa: E501
    """Add a new inventory item

     # noqa: E501

    :param body: Inventory item that needs to be added
    :type body: dict | bytes

    :rtype: None
    """
    return 'do some magic!'


def delete_inventory_item(itemID):  # noqa: E501
    """Deletes an inventory item

     # noqa: E501

    :param itemID: ID of inventory item to be deleted
    :type itemID: int

    :rtype: None
    """
    return 'do some magic!'


def get_all_invetory_items():  # noqa: E501
    """Get all inventory items

    Returns all inventory items # noqa: E501


    :rtype: List[InventoryItem]
    """
    return 'do some magic!'


def get_inventory_item_by_id(itemID):  # noqa: E501
    """Find inventory item by ID

    Returns a single inventory item # noqa: E501

    :param itemID: ID of inventory item to return
    :type itemID: int

    :rtype: InventoryItem
    """
    return 'do some magic!'


def update_inventory_item(body):  # noqa: E501
    """Update an existing inventory item

     # noqa: E501

    :param body: Inventory item that needs to be updated
    :type body: dict | bytes

    :rtype: None
    """
    return 'do some magic!'
