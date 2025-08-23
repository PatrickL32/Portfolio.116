"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:.
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  patJh('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from  django.conf import settings
from django.conf.urls.static import static
# In your project's main urls.py (e.g., config/urls.py)

urlpatterns = [
    # Add this line for the homepage
    path('', views.home_view, name='home'),

    # Your existing URLs
    path('admin/', admin.site.urls),
    path('about/', ... ), # Assumes you have an 'about' view
    path('projects/', ... ), # Assumes you have a 'projects' view
    # ... other paths
]

urlpatterns+=static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)