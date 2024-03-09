app_name = 'accounts'
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.QuestLogin, name='QuestLogin'),
    path('register/', views.QuestRegister, name='QuestRegister'),
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
    path('logout/', views.user_logout, name='user_logout'),
]
