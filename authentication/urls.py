from authentication import views

from django.urls import path

urlpatterns = [
	path('user-login/', views.UserLogin.as_view(), name='user-login'),
	path('register-user/', views.RegisterUser.as_view(), name='register-user'),
	path('update-user-details/', views.UpdateUserDetails.as_view(), name='update-user-details'),
	path('forgot-password/', views.ForgotPassword.as_view(), name='forgot-password'),
	path('delete-user/', views.DeleteUser.as_view(), name='delete-user'),
]
