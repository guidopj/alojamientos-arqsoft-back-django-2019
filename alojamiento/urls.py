from django.urls import path
from . import views

urlpatterns = [
    path('create_accommodation', views.create_accommodation, name="create_accommodation")
]