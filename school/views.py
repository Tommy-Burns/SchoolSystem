from django.shortcuts import render
from django.http import HttpResponse as HR
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
        return render(request, 'index.html', {'null': null_text})
    else:
        return render(request, 'index.html', {
            'courses': courses,
            'searchTerm': searchTerm,
        })


