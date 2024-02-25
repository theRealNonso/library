from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from api.models import Book
from api.serializers import BookSerializer


class BookTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.book_data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'genre': 'Test Genre',
            'published_date': '2024-01-01',
            'isbn': '1234567890'
        }
        self.book = Book.objects.create(**self.book_data)

    def test_create_book(self):
        response = self.client.post(reverse('book-list-create'), self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_all_books(self):
        response = self.client.get(reverse('book-list-create'))
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_book(self):
        response = self.client.get(reverse('book-detail', args=[self.book.id]))
        book = Book.objects.get(pk=self.book.id)
        serializer = BookSerializer(book)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_book(self):
        updated_data = {
            'title': 'Updated Title',
            'author': 'Updated Author',
            'genre': 'Updated Genre',
            'published_date': '2024-01-01',
            'isbn': '0987654321'
        }
        response = self.client.put(reverse('book-detail', args=[self.book.id]), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        response = self.client.delete(reverse('book-detail', args=[self.book.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_single_book_not_found(self):
        response = self.client.get(reverse('book-detail', args=[1000]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_book_not_found(self):
        updated_data = {
            'title': 'Updated Title',
            'author': 'Updated Author',
            'genre': 'Updated Genre',
            'published_date': '2024-01-01',
            'isbn': '0987654321'
        }
        response = self.client.put(reverse('book-detail', args=[1000]), updated_data,
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_book_not_found(self):
        response = self.client.delete(reverse('book-detail', args=[1000]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
