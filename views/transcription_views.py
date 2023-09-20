from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from forms import TranscriptionForm
from models import TranscriptionRequest
from transcription_results import generate_summary


def update_transcription(request):
    if request.method == 'POST':
        transcription_text = request.POST.get('transcription_text')
        summary = generate_summary(transcription_text)
        return JsonResponse({'summary': summary})


def transcription_history(request):
    user_requests = TranscriptionRequest.objects.filter(user=request.user)

    # Pass the list of user-specific transcription requests to the template
    context = {'user_requests': user_requests}
    return render(request, 'yourappname/transcription_history.html', context)


def get(request, pk):
    try:
        transcription = TranscriptionRequest.objects.get(pk=pk, user=request.user)
        summary = generate_summary(transcription.transcription_text)  # Replace with your summary generation logic
        return Response({'summary': summary}, status=status.HTTP_200_OK)
    except TranscriptionRequest.DoesNotExist:
        return Response({'error': 'Transcription not found.'}, status=status.HTTP_404_NOT_FOUND)


class TranscriptionSummaryView(APIView):
    pass


def post(request):
    form = TranscriptionForm(request.data)
    if form.is_valid():
        # Save the transcription or perform further processing
        return Response({'message': 'Transcription created successfully.'}, status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


class TranscriptionCreateView(APIView):
    pass
