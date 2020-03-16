"""django1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from home.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('m/',include("home.urls")),
    path('django0316/',include("django0316.urls")),
    path('summernote/', include('django_summernote.urls')),
    path('allauth1/', include('allauth1.urls')),
    path('accounts/',include('allauth.urls')),
    path('ajax/',include('home_ajax.urls'))
]

