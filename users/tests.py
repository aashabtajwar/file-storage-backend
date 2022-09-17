from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase

# Create your tests here.

class TestSetup(APITestCase):
    
    def setUp(self):
        self.register_url = reverse('register')
        user_data = {
            'email': 'email@gmail.com',
            'username': 'email',
            'first_name': 'emailed',
            'last_name': 'user',
            'password': 'testing111'
        }

        # we are overwriting setUp and tearDown() methods
        # so we are calling super() for each
        return super().setUp()

    def tearDown(self):
        return super().tearDown()


class TestViews(TestSetup):
    
    def test_user_cannot_register_with_no_data(self):
        # APITestCase inherits APIClient
        # testing that a user cannot register without data
        response = self.client.post(self.register_url)
        self.assertEqual(response.status_code, 400)