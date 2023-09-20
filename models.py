from django.db import models
from django.contrib.auth.models import User


class TranscriptionRequest(models.Model):
    """
    Represents a user's transcription request.
    """
    transcription_text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    youtube_url = models.URLField(null=True, blank=True)
    audio_file = models.FileField(upload_to='audio_files/', null=True, blank=True)
    requested_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()  # Make sure the objects manager is defined


class RefinedTranscription(models.Model):
    """
    Represents a refined transcription based on the user's request.
    """
    transcription_request = models.OneToOneField(TranscriptionRequest, on_delete=models.CASCADE)
    transcription = models.TextField()
    language = models.CharField(max_length=10)
    refined_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()  # Define the objects manager


class TranscriptionSummary(models.Model):
    """
    Represents a summary of a refined transcription.
    """
    refined_transcription = models.OneToOneField(RefinedTranscription, on_delete=models.CASCADE)
    summary = models.TextField()
    objects = models.Manager()  # Define the objects manager


class UserProfile(models.Model):
    """
    Represents additional user profile information.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_language = models.CharField(max_length=10)
    objects = models.Manager()  # Define the objects manager
