from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework.test import APITestCase
from django.test import TestCase

import os

# Create your tests here.
class TestSetup(APITestCase):
    def setUp(self):
        self.upload_url = reverse('upload-file-v2')
        token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjU2NjE1OTIuMjA3OTY5LCJ1c2VybmFtZSI6ImFhc2hhYiIsImVtYWlsIjoiaHFodW50ZXI3ODBAZ21haWwuY29tIiwiaWQiOjEsInR5cGUiOiJhY2Nlc3MifQ.MF0aCo79avNUJNrHVCFfl2jkqphLPpqXHuGZiD1GRJE'
        self.header = {
            'HTTP_AUTHORIZATION': token
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

class TestViews(TestSetup):
    def test_can_uplad_file(self):
        file = SimpleUploadedFile(os.path.abspath('/test-files/doc.pdf'), b"file_content", content_type='application/pdf')
        response = self.client.post(self.upload_url, {'file':file}, **self.header)
        self.assertEqual(response.status_code, 200)
        # pass