from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework.test import APITestCase
from django.test import TestCase

import os

# Create your tests here.
class TestSetup(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('user-login')
        self.user_data = {
            'email': 'hqhunter780@gmail.com',
            'username': 'aashab',
            'first_name': 'aashab',
            'last_name': 'tajwar',
            'password': 'testing111'
        }
        self.login_data = {
            'email' : 'hqhunter780@gmail.com',
            'password': 'testing111',
        }
        self.upload_url = reverse('upload-file-v2')
        token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjU3MzIxMTUuNDUyNzE5MiwidXNlcm5hbWUiOiJhYXNoYWIiLCJlbWFpbCI6ImhxaHVudGVyNzgwQGdtYWlsLmNvbSIsImlkIjoxLCJ0eXBlIjoiYWNjZXNzIn0.EzQvgLAkRulDNJepJGCFMk2d3qIhtMKufGxQTS87SX4'
        self.header = {
            'HTTP_AUTHORIZATION': token
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

class TestViews(TestSetup):
    def test_can_upload_file(self):
        registrationResponse = self.client.post(self.register_url, self.user_data, format="json")
        loginResponse = self.client.post(self.login_url, self.login_data, format="json")
        # headers = {
        #     'HTTP_AUTHORIZATION': loginResponse.access_token
        # }
        file = SimpleUploadedFile(os.path.abspath('/test-files/doc.pdf'), b"file_content", content_type='application/pdf')
        response = self.client.post(self.upload_url, {'file':file}, **self.header)
        self.assertEqual(response.status_code, 200)
        # pass