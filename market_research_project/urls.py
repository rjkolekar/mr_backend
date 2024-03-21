
# projectname/urls.py

from django.contrib import admin
from django.urls import path, include
from authentication.views import register_user

urlpatterns = [
    path('admin/', admin.site.urls),
      path('api/register/', register_user, name='register_user'),
    path('accounts/', include('django.contrib.auth.urls')),  # Built-in authentication views
    # Add your custom authentication URLs here if needed
     path('api/', include('reports.urls')),
]