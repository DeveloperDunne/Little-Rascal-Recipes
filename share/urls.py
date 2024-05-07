from .import views
from django.urls import path
urlpatterns = [
    path('', views.Share,
         name='share'),
]