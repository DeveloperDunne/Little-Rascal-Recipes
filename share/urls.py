from .import views
from django.urls import path

urlpatterns = [
    path('', views.share_a_book,
         name='share'),
    path('<slug:slug>/edit_share/<int:share_id>', views.share_edit, name='share_edit'),
    path('<slug:slug>/delete_share/<int:share_id>', views.share_delete, name='share_delete'),
]