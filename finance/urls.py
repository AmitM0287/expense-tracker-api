from django.urls import path
from finance import views

urlpatterns = [
	path('userInvestments/', views.UserInvestments.as_view(), name='userInvestments'),
	path('userSavings/', views.UserSavings.as_view(), name='userSavings'),
	path('userExpences/', views.UserExpences.as_view(), name='userExpences'),
	path('downloadExcel/', views.DownloadExcel.as_view(), name='downloadExcel'),
]
