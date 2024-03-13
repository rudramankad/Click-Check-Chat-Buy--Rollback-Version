app_name = 'index'
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.elcetronic, name='electronic'),
    path('buypage/<int:item_id>/', views.buypage, name='buypage'),
    path('uploaditem/', views.uploaditem, name='uploaditem'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('chat', views.chat, name='chat'),
    path('myprofile/', views.my_profile, name='my_profile'),
]
