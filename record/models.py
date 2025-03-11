from django.db import models
from book.models import Book
from user.models import Member

# Create your models here.

class BorrowedRecord(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=False)
    return_date = models.DateTimeField(null=True, blank=True)
    BORROW_TYPE_STATUS = [
        ('borrowed', 'Borrowed'),
        ('returned', 'Returned'),
        ('overdue', 'Overdue'),
    ]
    borrow_status = models.CharField(max_length=20, choices=BORROW_TYPE_STATUS, default='borrowed')
    overdue_fine_count = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.borrow_status