from django.urls import path
from . import views

urlpatterns = [
    path('', views.lab_portal_home, name=''),
]