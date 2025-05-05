from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core.views import index, contact  # Import the views from the core app

urlpatterns = [
    
    path('', index, name='index'),
    path('items/', include('item.urls')),  # Include item app URLs with namespace
    path('contact/',contact, name ='contact'),
    path('admin/', admin.site.urls),
     # Add this line to include the index view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Serve media files in development
# This line is used to serve media files during development. In production, you would typically use a web server like Nginx or Apache to serve static and media files.
