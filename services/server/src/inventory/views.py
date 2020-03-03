from connexion import request
from flask import make_response, jsonify
from sqlalchemy.exc import IntegrityError

from src import db
from src.models import Product


def add_product(body):
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
            try:
                db.session.add(new_product)
                db.session.commit()
                return make_response(
                    'New product successfully created',
                    201
                )
            except IntegrityError:
                return make_response(
                    'A product with that name already exists',
                    409
                )
        else:
            return make_response(
                f'Product, {name}, already exists',
                409
            )


def delete_product(productID):
    product = db.session.query(Product).filter_by(id=productID)

    if product.one_or_none() is None:
        return make_response('Product not found', 404)

    product.delete()
    db.session.commit()

    return make_response('Product successfully deleted', 200)


def get_all_products():
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


def get_product_by_id(productID):
    result = db.session.query(Product).filter_by(id=productID).first()

    if result is None:
        return make_response('Product not found', 404)

    product = {
        'id': result.id,
        'name': result.name,
        'description': result.description,
        'quantity': result.quantity,
        'price': result.price
    }

    return make_response(product, 200)


def update_product(body):
    if request.is_json:
        id = body.get('id')
        name = body.get('name')
        description = body.get('description')
        quantity = body.get('quantity')
        price = body.get('price')

        product = db.session.query(Product).filter_by(id=id)

        data = {
            'id': id,
            'name': name,
            'description': description,
            'quantity': quantity,
            'price': price
        }

        product.update(data)
        db.session.commit()

        return make_response('Product information was updated', 201)
