# include all the app urls for the my_app part
from django.urls import path
from . import views

app_name = "my_app"

urlpatterns = [
    path('',views.index,name="index"),
]