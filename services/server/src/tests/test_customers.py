import unittest

from flask import json

from ..model.customer import Customer


class TestCustomer(unittest.TestCase):
    """CustomerController integration test stubs"""

    def test_add_customer(self):
        """Test case for add_customer

        Add a new customer
        """
        body = Customer()
        response = self.client.open(
            '/v1/customer',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_customer(self):
        """Test case for delete_customer

        Deletes a customer
        """
        response = self.client.open(
            '/v1/customer/{customerID}'.format(customerID=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_customers(self):
        """Test case for get_all_customers

        Get all customers
        """
        response = self.client.open(
            '/v1/customer/all',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_customer_by_id(self):
        """Test case for get_customer_by_id

        Find customer by ID
        """
        response = self.client.open(
            '/v1/customer/{customerID}'.format(customerID=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_customer(self):
        """Test case for update_customer

        Update an existing customer
        """
        body = Customer()
        response = self.client.open(
            '/v1/customer',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
