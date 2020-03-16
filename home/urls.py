from django.urls import path,include
from .views import *
urlpatterns=[
    path('',index,name="index"),
    path('signin', signin, name="signin"),
    path('signup', signup, name="signup"),
    path('home', home, name="home"),
    path('signout', signout, name="signout"),
    path('board', board, name="board"),
    path('k_logout/', k_logout, name="k_logout"),
    path('k_delete/', k_delete, name="k_delete"),
    path('select_me/', select_me, name="select_me"),
    path('oauth/', oauth),
]