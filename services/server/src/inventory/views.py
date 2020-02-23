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
    product = db.session.query(Product).filter_by(id=productID)

    if product.one_or_none() is None:
        abort(404, 'Product not found')

    product.delete()
    db.session.commit()

    return make_response('Product sucessfully deleted', 200)


def get_all_products():  # noqa: E501
    results = db.session.query(Product).order_by(Product.name.asc())
    all_products = []

    for result in results:
        product = {
            'id': result.id,
            'name': result.name,
            'description': result.description,
            'quantity': result.quantity,
            'price': result.price
        }
        all_products.append(product)

    return make_response(jsonify(items=all_products), 200)


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
