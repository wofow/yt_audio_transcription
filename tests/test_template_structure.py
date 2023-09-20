# tests/test_templates.py

from django.test import TestCase
from django.template import Template, Context

class TranscriptionResultsTemplateTest(TestCase):
    def test_transcription_results_template(self):
        template = Template('{% load yourappname_tags %}{% transcription_results_template %}')
        context = Context({})
        rendered = template.render(context)
        # Add assertions to check for expected content in the rendered HTML
