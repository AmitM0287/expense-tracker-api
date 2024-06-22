from django.urls import path
from authentication.views import UserLogin

urlpatterns = [
    path('userLogin/', UserLogin.as_view()),
]
