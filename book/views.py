from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from book.models import Book, Author, Category
from book.serializers import BooksSerializer, AuthorSerializer, CategorySerializer
from book.paginations import DefaultPagination
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

# Create your views here.

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    pagination_class = DefaultPagination
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]