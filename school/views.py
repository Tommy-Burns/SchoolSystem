import django
from django.shortcuts import render
from django.http import HttpResponse as HR
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Courses
from accounts.models import RegisteredCourses


# Create your views here.
def index(request):
    searchTerm = request.GET.get('searchCourse')
    null_text = "We couldn't find a course that matches your seach criteria."
    courses = Courses.objects.all()
    if request.user:
        username = request.user.username
        user_courses = RegisteredCourses.objects.filter(user_name=username)
        enroll_excluded = Courses.objects.filter(name__in=[i.registered_course for i in user_courses])
        not_enrolled = courses.difference(enroll_excluded)

        print('***********************COURSES********************', courses)
        print('***********************EXCLUDED COURSES********************', enroll_excluded)
        print('**********************NOT ENROLLED*********************', not_enrolled)
        return render(request, 'index.html', {
            'courses': courses,
            'enroll_excluded': enroll_excluded,
            'not_enrolled': not_enrolled,
        })
        
    if searchTerm:
        courses = Courses.objects.filter(name__icontains=searchTerm)       
    
    if len(courses) == 0:
        return render(request, 'index.html', {
            'null': null_text,
            'searchTerm': searchTerm,
            })
    else:
        return render(request, 'index.html', {
            'courses': courses,
            'searchTerm': searchTerm,
            # 'reg_courses': user_reg_courses,
        })


def details(request, course_id):
    course = get_object_or_404(Courses, pk=course_id)
    return render(request, 'details.html', {
        'course': course,
    })
    
def contact(request):
    return render(request, 'contact.html')


@login_required
def checkout(request, course_name):
    course = get_object_or_404(Courses, name=course_name)

    return render(request, 'checkout.html', {
        'course': course,
    })