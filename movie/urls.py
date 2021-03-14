from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('', views.index,name="index"),
    path('func/',views.function,name="function")
    ]
    