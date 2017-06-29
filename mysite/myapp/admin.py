# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from  .models import Author, Book, Course, Student, Topic

# Register your models here.
admin.site.register(Author)
admin.site.register(Course)
admin.site.register(Topic)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author', 'in_stock')
    def clean_num(self):
        numpages = self.cleaned_data.get('numpages')
        raise ValidationError("Number should between 50 and 1000")
admin.site.register(Book, BookAdmin)

class StudentAdmin(admin.ModelAdmin):
    model = Student
    list_display=('first_name','last_name', 'get_courses')
    def get_courses(self, obj):
        courses = obj.course_set.all()
        course_titles = ''
        for c in courses:
            course_titles = (c.title + ' ')

        return course_titles
    get_courses.admin_order_field = 'first_name'
    get_courses.short_description = 'courses'

admin.site.register(Student, StudentAdmin)
