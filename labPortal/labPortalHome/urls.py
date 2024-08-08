from django.urls import path
from . import views

urlpatterns = [
    path('', views.lab_portal_home, name=''),
    path('lab-rules', views.lab_rules, name='lab-rules'),
]