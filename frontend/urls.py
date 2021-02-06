from django.urls import path
from . import views

app_name = 'frontend'

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.index, name=''),
    path('join/', views.index, name='join'),
    path('info/', views.index, name='info'),
    path('create/', views.index, name='create'),
    path('room/<str:roomCode>', views.index, name='room-code'),

]
