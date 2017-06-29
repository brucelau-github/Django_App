# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from myapp.models import Author, Book, Course, Topic
from myapp.forms import TopicForm, InterestForm, RegisterForm, LoginForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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
def topics(request):
    topiclist = Topic.objects.all()[:10]
    return render(request, 'myapp/topics.html', {'topiclist': topiclist})

def addtopic(request):
    topiclist = Topic.objects.all()
    if request.method=='POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.num_responses=1
            topic.save()
            return HttpResponseRedirect(reverse('myapp:topics'))
    else:
        form=TopicForm()
    return render(request, 'myapp/addtopic.html', {'form':form, 'topiclist':topiclist})

def topicdetail(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    if request.method=='POST':
        form = InterestForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['interested'] == '1':
                topic.num_responses +=1
                topic.avg_age = (topic.avg_age + form.cleaned_data['age'])/(topic.num_responses)
                topic.save()
            return HttpResponseRedirect(reverse('myapp:topics'))
    else:
        form = InterestForm()
    return render(request, 'myapp/topicdetail.html', {'form':form, 'topic':topic})

def register(request):
    if(request.method=='POST'):
        form = RegisterForm(request.POST)
        if form.is_valid():
            uname = request.POST['username']
            pwd = request.POST['password']
            email = request.POST['email']
            student = Student.objects.create_user(uname,email,pwd)
            student = form.save(commit=False)
            student.save()
            user2 = authenticate(username='abs',password='123')
            student.username = uname
            student.password =pwd
            # student.first_name = request.POST['first_name']
            # student.last_name = request.POST['last_name']
            # student.save()
            # # Student.objects.create(user=student)
            # user = authenticate(username=student.username, password=student.password)
            # Student.objects.create_user(request.POST['username'],"", request.POST['password'], form.cleaned_data['age'])
            return HttpResponseRedirect(reverse('myapp:index'))
    else:
        print('GET')
        form = RegisterForm()
        return render(request, 'myapp/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('myapp:index'))
            else:
                return HttpResponse('Your account is disabled.')
        else:
            return HttpResponse('Invalid login details.')
    else:
        form = LoginForm()
        return render(request, 'myapp/login.html', {'form':form})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse(('myapp:index')))
