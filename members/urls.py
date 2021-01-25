from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('<int:port_num>',views.result),
    path('signup',views.signup),
    path('git',views.git),
    path('gugu',views.gu),
    path('login',views.login),
    path('logout',views.logout),
    path('members',views.login_after),
]
