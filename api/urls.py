from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView, # Generates a JSON token based on a user once we've reached the endpoint
    TokenRefreshView, # Generates a refresh token
)

urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # A token is stored in the browser somewhere and it generally has a short lifespan (This creates a longer lifespan of the token eg: 30 days)

    path('', views.getRoutes),
    path('projects/', views.getProjects),
    path('projects/<str:pk>/', views.getProject),
    path('projects/<str:pk>/vote/', views.projectVote),

    path('remove-tag/', views.removeTag)
]