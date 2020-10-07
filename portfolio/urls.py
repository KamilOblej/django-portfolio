from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<pk>/', views.details, name='details'),
    path('projects/', views.all_projects, name='projects'),
]
