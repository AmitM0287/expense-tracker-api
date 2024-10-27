from downloader import views
from django.urls import path

urlpatterns = [
	path('youtube/', views.YouTubeDownloader.as_view(), name='youtube'),
	path('video-splitter/', views.VideoSplitter.as_view(), name='videoSplitter'),
]
