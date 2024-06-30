from django.urls import path
from lifestyle import views

urlpatterns = [
    path('investments/', views.Investments.as_view()),
    path('savings/', views.Savings.as_view()),
    path('expences/', views.Expences.as_view()),
]
