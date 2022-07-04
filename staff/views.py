from django.shortcuts import render
from .models import Staff
from django.shortcuts import get_object_or_404

# Create your views here.
def staff(request):
    members = Staff.objects.all().order_by('name')
    return render(request, 'staff.html', {
        'members': members,
    })
    
def staff_details(request, staff_id):
    staff = get_object_or_404(Staff, pk=staff_id)
    return render(request, 'staff-details.html', {
        'staff': staff,
    })


