from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=255, null=False)
    biograpy = models.TextField()
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    isbn = models.CharField(max_length=20, unique=True, null=False)
    title = models.CharField(max_length=255, null=False)
    publication_year = models.DateField()
    publisher = models.CharField(max_length=255)
    edition = models.CharField(max_length=100)
    total_copies = models.PositiveIntegerField(default=1)
    available_copies = models.PositiveIntegerField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    description = models.TextField()
    # cover_image_url
    added_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def clean(self):
        super().clean()

        if self.available_copies > self.total_copies:
            raise ValidationError({
                "available_copies": "Available copies can't be greater than total copies"
            })
        
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

