from sourceSync import views

from django.urls import path

urlpatterns = [
	path('syncGoogleSheet/', views.SyncGoogleSheet.as_view(), name='syncGoogleSheet'),
]
