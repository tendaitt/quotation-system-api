import unittest

from flask import json

from ..model.product import Product


class TestInventory(unittest.TestCase):
    """InventoryController integration test stubs"""

    def test_add_product(self):
        """Test case for add_product

        Add a new product
        """
        body = Product()
        response = self.client.open(
            '/v1/inventory',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_product(self):
        """Test case for delete_product

        Deletes a product
        """
        response = self.client.open(
            '/v1/inventory/{productID}'.format(productID=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_products(self):
        """Test case for get_all_products

        Get all products
        """
        response = self.client.open(
            '/v1/inventory/all',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_product_by_id(self):
        """Test case for get_product_by_id

        Find product by ID
        """
        response = self.client.open(
            '/v1/inventory/{productID}'.format(productID=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_product(self):
        """Test case for update_product

        Update an existing product
        """
        body = Product()
        response = self.client.open(
            '/v1/inventory',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
