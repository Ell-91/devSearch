from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'), #set first parameter as an empty string to make it our home page
    path('project/<str:pk>/', views.project, name='project'),

    path('create-project/', views.createProject, name = "create-project"),
    path('update-project/<str:pk>/', views.updateProject, name="update-project"),
    path('delete-project/<str:pk>/', views.deleteProject, name="delete-project"),
]