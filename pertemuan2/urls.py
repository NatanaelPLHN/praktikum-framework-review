from django.urls import path
from . import views

app_name = 'pertemuan2'

urlpatterns = [
    path('about', views.about),
    path('', views.homepage),
    path('student/', views.student_index, name='student_index'),
    path('student/create/', views.student_create, name='student_create'),# Create
    path('student/update/<int:student_id>/', views.student_update, name='student_update'),
    path('student/delete/<int:student_id>/', views.student_delete, name='student_delete'),
]
