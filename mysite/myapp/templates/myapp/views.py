# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from myapp.models import Author, Book, Course

# Create your views here.
def index(request):
    courselist = Course.objects.all().order_by('title')[:10]
    return render(request, 'myapp/index.html', {'courselist': courselist})

def about(request):
    return render(request, 'myapp/about.html')

def detail(request, course_no):
    response = HttpResponse()
    #course = getCourse.objects.get(pk=course_no) #basic
    course = get_object_or_404(Course, pk=course_no)
    return render(request, 'myapp/detail.html',{'course': course})
