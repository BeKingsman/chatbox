from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('<int:pk>/message',views.Chat, name='chat'),
]