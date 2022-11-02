from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='home'),
    path('projects/<str:pk>/', views.project, name='projects'),
    path('create-project/', views.create_project, name='create-project'),
    path('update-project/<str:pk>/',views.update_project,name = 'update-project'),
    path('delete-project/<str:pk>/', views.delete_project, name='delete-project'),

]
