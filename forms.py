from django import forms
from django.urls import reverse

from models import TranscriptionRequest  # Make sure to import your TranscriptionRequest model
from django.shortcuts import render


def index(request):
    """
    Handle the index page view.
    """
    if request.method == 'POST':
        youtube_url = request.POST.get('youtube_url')
        audio_file = request.FILES.get('audio_file')

        # Perform Whisper JAX API request for transcription
        # Store transcription request in the database

    template_name = reverse('index')  # Fetch the template name dynamically
    return render(request, template_name)


class TranscriptionForm(forms.ModelForm):
    """
    Form for creating a transcription request.
    """
    class Meta:
        model = TranscriptionRequest
        fields = ['transcription_text']
