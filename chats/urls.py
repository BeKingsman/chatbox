from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('<int:pk>/message', views.Chat, name='chat'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
]
