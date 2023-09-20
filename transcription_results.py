from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from nltk.tokenize import sent_tokenize

from models import TranscriptionRequest, RefinedTranscription, TranscriptionSummary


def generate_summary(text):
    sentences = sent_tokenize(text)
    summary = " ".join(sentences[:3])  # Get the first 3 sentences as the summary
    return summary


@login_required
def transcription_results(request):
    if request.method == 'POST':
        transcription = request.POST.get('transcription')
        summary = generate_summary(transcription)
        selected_language = request.POST.get('language')

        audio_file = request.FILES.get('audio_file')
        if audio_file:
            fs = FileSystemStorage()
            audio_path = fs.save(audio_file.name, audio_file)

            transcription_request = TranscriptionRequest.objects.create(
                user=request.user,
                youtube_url=request.POST.get('youtube_url'),
                audio_file=audio_path
            )

            refined_transcription = RefinedTranscription.objects.create(
                transcription_request=transcription_request,
                transcription=transcription,
                language=selected_language
            )

            TranscriptionSummary.objects.create(
                refined_transcription=refined_transcription,
                summary=summary
            )

            return render(request, 'yourappname/transcription_results.html',
                          {'transcription': transcription, 'summary': summary})

        # Handle other form submission cases or errors

    # Handle GET requests or other cases
    return redirect('dashboard')  # Redirect to the dashboard view

# No need for the DashboardView if not used in this module


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'yourappname/dashboard.html'
