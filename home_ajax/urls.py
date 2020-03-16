from django.urls import path
from .views import *
urlpatterns=[
    path('ajax1/',ajax1,name="ajax1"),
    path('ajax1_basic/',ajax1_basic,name="ajax1_basic"),
]