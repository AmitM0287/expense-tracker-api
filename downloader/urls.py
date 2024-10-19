from downloader import views
from django.urls import path

urlpatterns = [
	path('youtube/', views.YouTubeDownloader.as_view(), name='youtube'),
]
