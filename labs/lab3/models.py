from django.db import models
import datetime
from django.contrib.auth.models import User
class Author(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    birthdate = models.DateField()
    age = models.IntegerField()
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author)
    in_stock = models.BooleanField(default=True)
class Student(User):
    PROVINCE_CHOICES = (
            ('AB','Alberta'), # First value is stored in db, the second is descriptive
            ('MB', 'Manitoba'),
            ('ON', 'Ontario'),
            ('QC', 'Quebec'),
            )
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=20, default='Windsor')
    province=models.CharField(max_length=2, choices=PROVINCE_CHOICES, default='ON')
    age = models.IntegerField()
