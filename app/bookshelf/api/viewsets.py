from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from app.bookshelf.models import Author, Book
from app.bookshelf.api.serializers import AuthorSerializer, BookSerializer
import requests
import json


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)