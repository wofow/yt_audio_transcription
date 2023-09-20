# tests/test_forms.py

from django.test import TestCase
from yourappname.forms import TranscriptionForm

class TranscriptionFormTest(TestCase):
    def test_form_valid(self):
        form = TranscriptionForm(data={'transcription_text': 'Sample transcription'})
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form = TranscriptionForm(data={})  # Empty data should be invalid
        self.assertFalse(form.is_valid())
