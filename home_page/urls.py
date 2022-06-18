from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('message_from_principal', views.message_from_principal, name='message_from_principal'),
    path('about', views.about, name='about'),

]
