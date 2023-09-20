# yourappname/api/tests/test_authentication.py

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthenticationAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.transcription_data = {'transcription_text': 'Sample transcription'}

    def test_authenticated_access(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(reverse('transcription-create'), data=self.transcription_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unauthenticated_access(self):
        response = self.client.post(reverse('transcription-create'), data=self.transcription_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
