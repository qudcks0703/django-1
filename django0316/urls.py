from django.urls import path,include
from .views import *
urlpatterns=[
    path('',index,name='index'),
    path('room/<str:room_name>/',room,name='room'),
    path('board/',board,name='board'),
]