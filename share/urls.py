from .import views
from django.urls import path
urlpatterns = [
    path('', views.share_a_book,
         name='share'),
]