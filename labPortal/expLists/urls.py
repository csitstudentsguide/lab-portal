from django.urls import path
from . import views

urlpatterns = [
    path('', views.expLists_home, name="expLists-home"),
    path('upload-exp/', views.upload_exp, name='upload-exp'),
    path('show-expl-lists/', views.show_exp_lists, name='show-expl-lists'),
]