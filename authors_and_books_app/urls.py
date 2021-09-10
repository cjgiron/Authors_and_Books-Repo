from django.urls import path     
from . import views


urlpatterns = [
    path('', views.index),
    path('process_book', views.process_book),
    path('books/<int:book_id>/delete', views.delete),   
]