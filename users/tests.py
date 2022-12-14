from http import client
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase

# Create your tests here.

class TestSetup(APITestCase):
    
    # method called before carrying out a test case
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('user-login')
        self.user_data = {
            'email': 'email@gmail.com',
            'username': 'email',
            'first_name': 'emailed',
            'last_name': 'user',
            'password': 'testing111'
        }
        self.login_data = {
            'email' : 'email@gmail.com',
            'password': 'testing111',
        }
        # we are overwriting setUp and tearDown() methods
        # so we are calling super() for each
        return super().setUp()

    # called after a test case is completed
    def tearDown(self):
        return super().tearDown()


class TestViews(TestSetup):
    
    def test_user_cannot_register_with_no_data(self):
        # APITestCase inherits APIClient
        # testing that a user cannot register without data
        response = self.client.post(self.register_url)
        self.assertEqual(response.status_code, 400)

    def test_user_can_register(self):
        # test that a user can register with data
        response = self.client.post(self.register_url, self.user_data, format="json")
        # import pdb
        # pdb.set_trace()

        self.assertEqual(response.data['message'], 'Registration Success')
        self.assertEqual(response.status_code, 201)

    def test_user_can_login(self):
        # login cannot work before registering first

        registrationResponse = self.client.post(self.register_url, self.user_data, format="json")
        loginResponse = self.client.post(self.login_url, self.login_data, format="json")
        print(loginResponse.get('access_token'))
        # import pdb
        # pdb.set_trace()
        self.assertEqual(loginResponse.status_code, 200)












# class TestLoginSetup(APITestCase):
#     def setUp(self):
#         self.login_url = reverse('user-login')
#         self.user_data = {
#             'email': 'hqhunter780@gmail.com',
#             'password': 'testing111',
#         }
#         return super().setUp()
    
#     def tearDown(self):
#         return super().tearDown()

# class LoginTestViews(TestLoginSetup):
#     def test_user_can_login(self):
#         response = self.client.post(self.login_url, self.user_data, format = "json")
#         self.assertEqual(response.data['message'], 'Okay')