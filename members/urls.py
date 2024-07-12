from django.urls import path
from . import views

urlpatterns = [
    path('', views.members),
    path('members/', views.members, name='members'),
]