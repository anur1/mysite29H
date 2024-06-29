from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.index),
    path('<kurs_id>', views.details, name="course_details"),
    path('kategori/<int:category_id>', views.getCoursesByCategoryId),
    path('kategori/<str:category_name>', views.getCoursesByCategory, name='courses_by_category'),
]