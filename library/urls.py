from django.urls import path,include
from . import views

urlpatterns = [

    path('books/',views.book_list,name='book-list'),
    path('book/<int:pk>/',views.book_details,name='book-details'),
    path('collections/',views.collection_list,name='collection-list'),
    path('collection/<int:pk>/',views.collection_details,name='collection-details'),
    path('collection-create/',views.collection_create,name='collection-create'),
    path('collection-book-remove/<int:book_pk>/',views.collection_book_remove,name='collection-book-remove'),
     
]
