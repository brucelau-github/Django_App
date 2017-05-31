# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from myapp.models import Author, Book, Course

# Create your views here.
def index(request):
    couselist = Course.objects.all()[:10]
    response = HttpResponse()
    heading1 = '<p>' + 'List of courses:' + '</p>'
    response.write(heading1)
    for course in couselist:
        para = '<p>' + str(course) + '</p>'
        response.write(para)
    authorlist = Author.objects.all().order_by('birthdate')[:10]
    heading2 = '<p>' + 'List of author:' + '</p>'
    response.write(heading2)
    for author in authorlist:
        para1 = '<p>' + str(author) + '</p>'
        response.write(para1)
    return response

def about(request):
    response = HttpResponse()
    response.write('This is a Course Listing APP.')
    return response

def detail(request, course_no):
    response = HttpResponse()
    #course = getCourse.objects.get(pk=course_no) #basic
    course = get_object_or_404(Course, pk=course_no)
    para = '<p> Title:' + str(course.title) + '</p>'
    para += '<p> Course Number:' + str(course.course_no) + '</p>'
    txtBook = course.textbook
    para += '<p> Course Number:' + str(course.textbook.title) + '</p>'
    response.write(para)
    return response
