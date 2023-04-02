
from django.urls import path,include
from . import views
from .views import *

app_name = 'main'

urlpatterns = [
    path('',index,name="index"),
    path('home',home,name="home"),
    path('track',track,name="track")
]