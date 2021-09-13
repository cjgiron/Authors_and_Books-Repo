from django.urls import path     
from . import views


urlpatterns = [
    path('', views.index),
    path('process_book', views.process_book),
    path('books/<int:book_id>/delete', views.delete), 
    path('books/<int:book_id>/display', views.display),  
    path('add_author', views.add_author),
    path('authors', views.authors),
    path('process_author', views.process_author),
    path('authors/<int:author_id>/delete', views.delete_author),
    path('authors/<int:author_id>/display', views.display_author),
    path('add_book', views.add_book),
]