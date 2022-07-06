from django.urls import path
from . import views



urlpatterns = [
    path('', views.staff, name="staff"),
    path('<str:staff_name>/', views.staff_details, name="staff_details"),
]
