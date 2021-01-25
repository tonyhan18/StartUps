from django.urls import path
from . import views

urlpatterns=[
    path('<str:char1>/<str:char2>/',views.novel),
    path('',views.novel),
    path('<str:char1>/',views.novel),
]
