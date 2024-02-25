# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
import api.models as am
from django.http import Http404
import api.serializers as aps


class BookListCreate(generics.ListCreateAPIView):
    queryset = am.Book.objects.all()
    serializer_class = aps.BookSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = am.Book.objects.all()
    serializer_class = aps.BookSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404("Book not found")

    def get(self, request, *args, **kwargs):
        book = self.get_object()
        serializer = self.get_serializer(book)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        book = self.get_object()
        serializer = self.get_serializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        book = self.get_object()
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
