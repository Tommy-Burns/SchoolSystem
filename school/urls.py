from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('<str:course_name>', views.details, name='details'),
    path('checkout/<str:course_name>/', views.checkout, name='checkout'),
]