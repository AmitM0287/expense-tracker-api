from django.urls import path
from authentication import views

urlpatterns = [
    path('userLogin/', views.UserLogin.as_view()),
    path('userRegister/', views.UserRegister.as_view()),
]
