from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('countword', views.countword, name='countword'),
    path('about', views.about, name='about'),
]