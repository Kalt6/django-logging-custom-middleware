from django.urls import path
from . import views as userview   


urlpatterns = [
	path('home', userview.Home.as_view(), name='home')
]