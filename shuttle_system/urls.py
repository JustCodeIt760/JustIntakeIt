"""
URL configuration for shuttle_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.views.generic import RedirectView
from project_initiation.views import landing_page

urlpatterns = [
    path('', landing_page, name='landing'),  # Root URL now shows landing page
    path('admin/', admin.site.urls),
    path('dashboard/', include('project_initiation.urls')),  # Move project_initiation URLs under dashboard/
    path('requirements/', include('requirements_gathering.urls')),
    path('system-design/', include('system_design.urls')),
    path('chatbot/', include('chatbot.urls')),  # Add chatbot URLs
]
