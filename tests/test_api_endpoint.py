# yourappname/api/tests/test_transcription_api.py

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from yourappname.models import TranscriptionRequest

User = get_user_model()

class TranscriptionAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.transcription = TranscriptionRequest.objects.create(transcription_text='Sample transcription', user=self.user)

    def test_get_transcription_summary(self):
        url = reverse('transcription-summary', args=[self.transcription.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['summary'], 'Summary of the transcription')  # Replace with expected summary

    def test_get_transcription_summary_unauthorized(self):
        self.client.logout()
        url = reverse('transcription-summary', args=[self.transcription.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
