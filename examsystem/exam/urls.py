from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_login, name='login'),
    path('register/', views.student_register, name='register'),
    path('logout/', views.student_logout, name='logout'),
    path('exams/', views.exam_list, name='exam_list'),
    path('exam/<int:exam_id>/', views.take_exam, name='take_exam'),
    
]
