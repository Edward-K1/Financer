from .base import BaseTest
from django.contrib.auth import get_user_model
from rest_framework import status


class TestUsers(BaseTest):
    """
    Test user functionality
    """

    def test_user_model(self):
        user = self.create_user(self.test_user_data_1)
        user_count = self.user_model.objects.count()
        self.assertEqual(user_count, 1)

    def test_user_registration(self):
        """
        Tests the user registration endpoint
        """
        response = self.register_user(self.test_user_data_1)
        self.assertEqual(response.status_code, 201)
