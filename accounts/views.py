import random
from django.shortcuts import get_object_or_404, render
from .forms import UserCreateForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

from .models import UserRegCourses
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

@login_required
def user_dashboard(request):
    username = request.user.username
    user_courses = UserRegCourses.objects.filter(user_name=username)
    courses = []
    for course in user_courses:
        course_to_add = Courses.objects.filter(name=course.registered_course)
        if course_to_add not in courses:
            courses.append(course_to_add)
        else:
            courses.append(course_to_add)
    return render(request, 'dashboard.html', {
        'courses': courses,
    })
    
    
def save_course(request):
    if request.method == 'GET':
        return render(request, 'checkout.html',{})            
    else:
        try:
            reg_course = UserRegCourses.objects.create(
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

@login_required
def resume_course(request, course_name):
    course = get_object_or_404(Courses, name=course_name)
    rangge = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen']
    rangge1 = range(4)
    num = random.randint(35, 95)
    return render(request, 'course_page.html', {
        'course': course,
        'rangge': rangge,
        'rangge1': rangge1,
        'num': num,
    })


@login_required
def user_profile(request, user_name):
    user_name = request.user.username
    return render(request, 'profile.html', {})


@login_required
def delete_course(request, course_id):
    course = get_object_or_404(UserRegCourses, field_name=course_id)
    print('*****************COURSE******************', course)
    # course.delete()
    return redirect('dashboard')
