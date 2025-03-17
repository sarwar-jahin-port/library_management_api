from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
from datetime import timedelta
# Create your models here.

class Member(AbstractUser):
    phone_number = models.CharField(max_length=13, validators=[
        RegexValidator(
                regex=r'^1\d{8,9}$',
                message="Enter a valid Bangladeshi phone number starting with '1' and followed by 8 or 9 digits.",
                code='invalid_bd_phone_number' # Optional error code
            )
    ])
    address = models.TextField()
    membership_date = models.DateTimeField(default=timezone.now)
    membership_expiry_date = models.DateTimeField(default=timezone.now()+timedelta(days=30))
    MEMBER_TYPE_CHOICES = [
        ('regular', 'Regular'),
        ('student', 'Student'),
        ('faculty', 'Faculty'),
        ('stuff', 'Stuff'),
    ]
    member_type = models.CharField(max_length=50, choices=MEMBER_TYPE_CHOICES, default='regular')

    def __str__(self):
        return self.username