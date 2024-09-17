from django.urls import path
from . import views

app_name = 'pertemuan2'

urlpatterns = [
path('about', views.about),
path('', views.homepage),
]