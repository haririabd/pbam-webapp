"""
URL configuration for arvmain project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from . import views

ON_CODESPACE = settings.ON_CODESPACE

urlpatterns = [
    path('admin/', admin.site.urls),
    # Allauth path
    path('accounts/', include('allauth.urls')),
    # Application path
    path('', views.index_view, name='index'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    # Forms only for swap
    path('contact-form-only/', views.contact_form_only, name='contact_form_only'),
]

if ON_CODESPACE:
    urlpatterns += [
        path('__reload__/', include("django_browser_reload.urls")),
    ]