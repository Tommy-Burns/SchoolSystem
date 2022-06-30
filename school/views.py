import django
from django.shortcuts import render
from django.http import HttpResponse as HR
from django.shortcuts import get_object_or_404
from .models import Courses

# Create your views here.
def index(request):
    searchTerm = request.GET.get('searchCourse')
    null_text = "We couldn't find a course that matches your seach criteria."
    if searchTerm:
        courses = Courses.objects.filter(name__icontains=searchTerm)       
    else:
        courses = Courses.objects.all()
    if len(courses) == 0:
        return render(request, 'index.html', {
            'null': null_text,
            'searchTerm': searchTerm,
            })
    else:
        return render(request, 'index.html', {
            'courses': courses,
            'searchTerm': searchTerm,
        })


def details(request, course_id):
    course = get_object_or_404(Courses, pk=course_id)
    return render(request, 'details.html', {
        'course': course,
    })
    
def contact(request):
    return render(request, 'contact.html')

