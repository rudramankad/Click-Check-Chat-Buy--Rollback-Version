app_name = 'requests'
from django.urls import path
from . import views

urlpatterns = [
    path('', views.userrequests, name='requests'),
]
