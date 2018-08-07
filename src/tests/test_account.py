"""Unittests for the API."""
from rest_framework.test import APIClient, APITestCase


class AccountTests(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        user_data = {
            "username": "testuser",
            "email": "test@testuser.com",
            "password": "123123"
        }
        response = self.client.post('register/', user_data)
        self.assertEqual(201, response.status_code)
