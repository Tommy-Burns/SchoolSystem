from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_user, name='logout'),
    path('login/', views.login_user, name='login'),
    path('dashboard/', views.user_dashboard, name='dashboard'),
    path('save_course/', views.save_course, name='save_course'),
    path('resume-course/<str:course_name>/', views.resume_course, name='resume_course'),
    path('profile/<str:user_name>/', views.user_profile, name='user_profile'),
]
