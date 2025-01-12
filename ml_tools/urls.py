from ml_tools import views
from django.urls import path

urlpatterns = [
	path('text-to-speech/', views.TextToSpeech.as_view(), name='text-to-speech'),
]
