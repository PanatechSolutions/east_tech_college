from django.urls import path
from . import views

urlpatterns = [
    path('programmes/', views.programmes, name='programmes'),
    path('computing/', views.computing, name='computing'),
    path('business_school/', views.business, name='business'),
    path('Application_Letter', views.Application_Letter, name='Application_Letter'),
    path('submit_Application', views.submit_Application, name='submit_Application'),   

]
