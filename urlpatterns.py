from django.urls import path

import transcription_results
from views.user_views import index, async_transcription

urlpatterns = [
    path('', index, name='index'),
    path('transcription/', transcription_results.transcription_results, name='transcription_results'),
    path('async_transcription/', async_transcription, name='async_transcription'),
    # Add more URL patterns as needed
]
