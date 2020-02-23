from connexion import request
from flask import make_response, abort, jsonify

from src import db
from src.models import Product


def add_product(body):  # noqa: E501
    if request.is_json:
        name = body.get('name')
        description = body.get('description')
        quantity = body.get('quantity')
        price = body.get('price')

        new_product = Product(
            name=name,
            description=description,
            quantity=quantity,
            price=price
        )

        existing_product = Product.query\
            .filter(Product.name == name)\
            .filter(Product.description == description)\
            .one_or_none()

        if existing_product is None:
            db.session.add(new_product)
            db.session.commit()
            return make_response('New product successfully created', 201)
        else:
            abort(409, f'Product, {name}, already exists')


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
