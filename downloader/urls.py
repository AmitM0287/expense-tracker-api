from downloader import views
from django.urls import path

urlpatterns = [
	path('youtube-video/', views.YouTubeDownloader.as_view(), name='youtube-video'),
	path('video-splitter/', views.VideoSplitter.as_view(), name='video-splitter'),
	path('media-cleanup/', views.MediaCleanupView.as_view(), name='media-cleanup'),
]
