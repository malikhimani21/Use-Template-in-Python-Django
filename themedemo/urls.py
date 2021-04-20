from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='homekey'),
    path('about/', views.about, name='aboutkey')
]