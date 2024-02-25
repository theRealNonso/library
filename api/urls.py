from django.urls import path
import api.views as av

urlpatterns = [
    path('books/', av.BookListCreate.as_view(), name='book-list-create'),
    path('books/<int:pk>/', av.BookRetrieveUpdateDestroy.as_view(), name='book-detail'),
]

