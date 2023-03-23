from django.urls import path
from . import views

app_name = 'picknews'

urlpatterns = [
    path('', views.index, name='index')
]