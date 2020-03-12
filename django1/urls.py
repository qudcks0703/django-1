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
from django.urls import path
from home.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('m/signin',signin,name="signin"),
    path('m/signup',signup,name="signup"),
    path('m/home',home,name="home"),
    path('m/signout',signout,name="signout"),
    path('m/board',board,name="board"),
    path('k_logout/',k_logout,name="k_logout"),
    path('k_delete/',k_delete,name="k_delete"),
    path('select_me/',select_me,name="select_me"),
    path('oauth/',oauth),
]

