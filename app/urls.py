"""my URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_students, name='show_students'),
    path('add/', views.add_student, name='add_student'),
    # New URL pattern with the student ID as a parameter
    path('student/<int:student_id>/',
         views.show_student_by_id, name='show_student_by_id'),
    path('student/<int:student_id>/update/', views.update_student,
         name='update_student'),  # New URL pattern for updating student data
]
