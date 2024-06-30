from django.urls import path
from authentication import views

urlpatterns = [
    path('userLogin/', views.UserLogin.as_view()),
    path('userRegister/', views.UserRegister.as_view()),
    path('updateUser/', views.UpdateUser.as_view()),
    path('forgotPassword/', views.ForgotPassword.as_view()),
    path('deleteUser/', views.DeleteUser.as_view()),
]
