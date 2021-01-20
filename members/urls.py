from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('signup',views.signup),
    path('git',views.git),
    path('gugu',views.gu),
    path('login',views.login),
]
