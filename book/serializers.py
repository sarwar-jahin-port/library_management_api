from rest_framework import serializers
from book.models import Author, Category, Book

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'book_count', 'created_at', 'updated_at']

    book_count = serializers.IntegerField(read_only=True)

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'isbn', 'title', 'publication_year', 'publisher', 'edition', 'total_copies', 'available_copies', 'category_id', 'author_id', 'description', 'added_date', 'updated_date']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'biograpy', 'date_of_birth', 'nationality', 'created_at', 'updated_at']
