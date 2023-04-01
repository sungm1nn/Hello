from django.urls import path
from . import views

app_name = 'picknews'

urlpatterns = [
    path('', views.index, name='index'),
    path('subscription', views.subs, name='subs'),
    path('pop',views.popup, name='popup'),
]