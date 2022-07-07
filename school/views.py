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
    
    if searchTerm:
        
        courses = Courses.objects.all()
        searched_courses = Courses.objects.filter(name__icontains=searchTerm)       

        if len(searched_courses) == 0:
            return render(request, 'index.html', {
                'null': null_text,
                'searchTerm': searchTerm,
                })
        else:
            if request.user:        
                username = request.user.username
                user_courses = RegisteredCourses.objects.filter(user_name=username)
                enroll_excluded = searched_courses.filter(name__in=[i.registered_course for i in user_courses])
                found_courses = searched_courses.difference(enroll_excluded)
                
                if len(found_courses) == 0:
                    return render(request, 'index.html', {
                    'null': null_text + " If a course is already enrolled, it wouldn't appear here.",
                    'searchTerm': searchTerm,
                    })
                else:
                    return render(request, 'index.html', {
                        'found_courses': found_courses,
                        'searchTerm': searchTerm,
                    })
            else:
                return render(request, 'index.html', {
            'courses': searched_courses,
            })
    courses = Courses.objects.all()
    
    if request.user:        
        username = request.user.username
        user_courses = RegisteredCourses.objects.filter(user_name=username)
        enroll_excluded = Courses.objects.filter(name__in=[i.registered_course for i in user_courses])
        not_enrolled = courses.difference(enroll_excluded)

        # print('***********************COURSES********************', courses)
        # print('***********************EXCLUDED COURSES********************', enroll_excluded)
        # print('**********************NOT ENROLLED*********************', not_enrolled)
        return render(request, 'index.html', {
            'courses': courses,
            'enroll_excluded': enroll_excluded,
            'not_enrolled': not_enrolled,
        })
        
    else:
        return render(request, 'index.html', {
            'courses': courses,
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