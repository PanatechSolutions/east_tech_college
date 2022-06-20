from django.urls import path
from . import views

urlpatterns = [
    path('admissions', views.admissions, name='admissions'),
    path('online_application', views.apply_online, name='apply_online'),
    path('requirements', views.requirements, name='requirements'),    
    path('fees', views.fees, name='fees'),  
]
