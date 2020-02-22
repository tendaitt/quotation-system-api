import unittest

from flask import json

from ..model.quote import Quote


class TestQuote(unittest.TestCase):
    """QuoteController integration test stubs"""

    def test_create_quote(self):
        """Test case for create_quote

        Create a new quote
        """
        body = Quote()
        response = self.client.open(
            '/v1/quote',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_quote(self):
        """Test case for delete_quote

        Deletes a quote
        """
        response = self.client.open(
            '/v1/quote/{quoteID}'.format(quoteID=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_quotes(self):
        """Test case for get_all_quotes

        Get all quotes
        """
        response = self.client.open(
            '/v1/quote/all',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_quote_by_id(self):
        """Test case for get_quote_by_id

        Find quote by ID
        """
        response = self.client.open(
            '/v1/quote/{quoteID}'.format(quoteID=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
