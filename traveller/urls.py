from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('contactus.html', views.contactus, name='contact-page')
]
