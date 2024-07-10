from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('search', views.search, name='search'),
    path('<slug:slug>', views.details, name="course_details"),
    path('kategori/<slug:slug>', views.getCoursesByCategory, name='courses_by_category'),
]