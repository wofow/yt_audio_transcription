from django.urls import path

from login_registration import register, user_login, user_logout
from views.transcription_views import update_transcription, TranscriptionSummaryView, TranscriptionCreateView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('update_transcription/', update_transcription, name='update_transcription'),
    path('transcription/<int:pk>/summary/', TranscriptionSummaryView.as_view(), name='transcription-summary'),
    path('transcription/create/', TranscriptionCreateView.as_view(), name='transcription-create'),
    # ...
]
