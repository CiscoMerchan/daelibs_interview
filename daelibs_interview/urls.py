"""
URL configuration for daelibs_interview project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Include the app's URLs from the 'traffic_api' app
    # This line includes the URL patterns defined in 'traffic_api.urls' into the project
    # The first argument is an empty string, meaning that these URLs will be included at the root level of the project
    # The 'include' function is used to include the URLs from 'traffic_api.urls' module
    path('', include('traffic_api.urls')),
    path('admin/', admin.site.urls),
]
