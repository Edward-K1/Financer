from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model


class BaseTest(TestCase):
    """
    The server base test file
    """

    def setUp(self):
        self.client = APIClient()
        self.user_model = get_user_model()
        self.test_user_data_1 = {
            "first_name": "nada",
            "last_name": "nada",
            "email": "nada@gmail.com",
            "username": "nadauser1",
            "password": "nadauser1"
        }

    def create_user(self, payload):
        """Helper function to create a normal user via models
        
        Arguments:
            payload {dict} -- a json representation of a user
        """
        user = self.user_model.objects.create(**payload)
        user.save()
        return user

    def register_user(self, payload):
        """Helper function to register a normal user via api
        
        Arguments:
            payload {dict} -- a json respresentation of a user
        
        Returns:
            response -- [the user registration response
        """
        response = self.client.post('/users/register/', payload, format="json")
        return response
