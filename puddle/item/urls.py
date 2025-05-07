from django.urls import path
from .import views

  # Import the views from the core app
app_name = 'item'  # Define the app name for namespacing

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),  # URL pattern for item detail view
    # Add more URL patterns as needed
]