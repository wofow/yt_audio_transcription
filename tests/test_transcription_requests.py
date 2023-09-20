# tests/test_models.py

from django.test import TestCase
from yourappname.models import TranscriptionRequest

class TranscriptionRequestModelTest(TestCase):
    def setUp(self):
        self.transcription_request = TranscriptionRequest.objects.create(transcription_text='Sample transcription')

    def test_transcription_request_creation(self):
        self.assertEqual(self.transcription_request.transcription_text, 'Sample transcription')
        # Add more assertions for other fields
