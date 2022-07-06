from django.shortcuts import render
from .forms import UserCreateForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

from .models import RegisteredCourses
from school.models import Courses

# Create your views here.
def signup(request):    
    if request.method == 'GET':
        return render(request, 'signup.html',{'form':UserCreateForm})            
    else:
        if request.POST['password1'] == request.POST['password2']:
             try:
                user = User.objects.create_user(request.POST['username'],
                            password=request.POST['password1'],
                            email=request.POST['email'],
                            first_name=request.POST['first_name'],
                            last_name=request.POST['last_name'],
                            )
                user.save()
                login(request, user)
                return redirect('home')
             except IntegrityError:
                return render(request, 'signup.html',
                 {'form':UserCreateForm,
                 'error':'Username already taken. Choose new username.'})
        else:
            return render(request, 'signup.html', {
                'form': UserCreateForm,
                'error': 'Passwords do not match.'
            })

@login_required
def logout_user(request):
    logout(request)
    return redirect('home')


def login_user(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm,
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {
            'form': AuthenticationForm,
            'error': 'username and password do not match',
            })
        else:
            login(request, user)
            return redirect('index')

def user_dashboard(request):
    username = request.user.username
    user_courses = RegisteredCourses.objects.filter(user_name=username)
    courses = []
    for course in user_courses:
        course_to_add = Courses.objects.filter(name=course.registered_course)
        if course_to_add not in courses:
            courses.append(course_to_add)
        else:
            courses.append(course_to_add)
    # print('***********************COURSES********************', courses)
    # print('***********************COURSES -- 0 ********************', courses[0])
    return render(request, 'dashboard.html', {
        'courses': courses,
    })
    
    
def save_course(request):
    if request.method == 'GET':
        return render(request, 'checkout.html',{})            
    else:
        try:
            reg_course = RegisteredCourses.objects.create(
                user_name=request.user.username,
            registered_course=request.POST['coursename']
            )
            reg_course.save() 
            return redirect('dashboard')
        except IntegrityError:
                error = 'You have already registered this course'
                return render(request, 'checkout.html', {
                    'error': error,
                })

