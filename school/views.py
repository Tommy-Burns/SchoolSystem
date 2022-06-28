from django.shortcuts import render
from django.http import HttpResponse as HR
from .models import Courses

# Create your views here.
def index(request):
    courses = Courses.objects.all()
    return render(request, 'index.html', {
        'courses': courses,
    })


