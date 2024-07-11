from django.urls import path
from authentication import views

urlpatterns = [
    path('userLogin/', views.UserLogin.as_view(), name='userLogin'),
    path('registerUser/', views.RegisterUser.as_view(), name='registerUser'),
    path('updateUserDetails/', views.UpdateUserDetails.as_view(), name='updateUserDetails'),
    path('forgotPassword/', views.ForgotPassword.as_view(), name='forgotPassword'),
    path('deleteUser/', views.DeleteUser.as_view(), name='deleteUser'),
]
