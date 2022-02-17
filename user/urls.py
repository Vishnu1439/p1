from django.urls import path
from . import views
from django.urls.conf import include

urlpatterns = [
    path('index',views.index),
    path('home',views.home)
]

