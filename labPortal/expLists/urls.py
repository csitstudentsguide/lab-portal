from django.urls import path
from . import views

urlpatterns = [
    path('', views.expLists_home, name="expLists_home"),
]