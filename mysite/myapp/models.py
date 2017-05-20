# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    birthdate = models.DateField()
    city = models.CharField(null = True,max_length=100, blank=True )
    def __str__(self):
        return self.firstname + " " + self.lastname

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author)
    in_stock = models.BooleanField(default=True)
    numpages = models.IntegerField()
    def __str__(self):
        return self.title

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
    def __str__(self):
        return self.first_name + " " + self.last_name

class Course(models.Model):
    course_no = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    textbook = models.ForeignKey(Book)
    students = models.ManyToManyField(Student)
    def __str__(self):
        return self.title

