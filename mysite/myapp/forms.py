from django import forms
from myapp.models import Topic, Student

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['subject', 'intro_course', 'time', 'avg_age']
    time = forms.ChoiceField(widget=forms.RadioSelect, label='Preferred Time', choices=Topic.TIME_CHOICES)
    avg_age = forms.CharField(max_length=3, label='What is your age?')
    intro_course = forms.BooleanField(label='This should be an introductory level course')

class InterestForm(forms.Form):
    interested =  forms.ChoiceField(widget=forms.RadioSelect, choices=(('1','yes'),('2','no')))
    age = forms.IntegerField(initial='20')
    comments = forms.CharField(required=False, widget=forms.Textarea, label='Additional Comments')

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['address', 'city', 'province', 'age']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
