import django
from myapp.models import Author, Book, Course, Student
# 5.
# a. list all the books int the db
Book.objects.all()
# b. list all the authors int the db
Author.objects.all()
# c. list all the courses int the db
Course.objects.all()

# 6. Write queries to do the following.
# a. List all Authors whose first name is  ‘John’  
Author.objects.filter(firstname = 'John')
# b. List all Books whose has an author with first name  is ‘John’  
Book.objects.filter(author__firstname='John')
# c. List all Books with the word ‘Networks’ in its title.  
Book.objects.filter(title__contains = 'Networks')
# d. List all Books that have the word ‘Networks’ in its title and are used in a course  
Book.objects.filter(title__contains = 'Networks').filter(course__textbook__isnull=False)
# e. List all the Courses that use the book  'Python Programming'  
Course.objects.filter(textbook__title__exact = 'Python Programming')
# f. List the Authors born after 1978  
Author.objects.filter(birthdate__year__gt = 1978)
# g. List the Authors born in January  
Author.objects.filter(birthdate__month = 1)
# h. List the Courses that use a book written by Alan Jones  
Course.objects.filter(textbook__author__firstname='Alan', textbook__author__lastname='Jones')
# i. List the Books currently in stock 
Book.objects.filter(in_stock = True)
# j. List the Books written by Mary Hall
Book.objects.filter(author__firstname='Mary', author__lastname='Hall')
# k. Get the first name of the Author of the textbook used in course 567.   
Course.objects.get(course_no = 567).textbook.author.firstname
# l. List all students registered in course 567
Course.objects.get(course_no = 567).students.all()
# m. List all the courses the Josh is registered in. 
Student.objects.get(first_name='Josh', last_name='James').course_set.all()
# n. List the textbook used in the course that Luis is registered in
Student.objects.get(first_name='Luis').course_set.all()[0].textbook()
# o. List all students with last name ‘James’.
Student.objects.filter(last_name='James')
