# yourappname/tests/test_forms.py

from django.test import TestCase
from yourappname.forms import TranscriptionForm

class TranscriptionFormTest(TestCase):
    def test_valid_transcription_submission(self):
        form_data = {'transcription_text': 'Sample transcription'}
        form = TranscriptionForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_transcription_submission_empty(self):
        form_data = {}
        form = TranscriptionForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_invalid_transcription_submission_long_text(self):
        form_data = {'transcription_text': 'A' * 1000}  # Assuming max length is 255
        form = TranscriptionForm(data=form_data)
        self.assertFalse(form.is_valid())

    # Add more test cases for different form validation scenarios
