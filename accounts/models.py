from django.db import models

# Create your models here.
class RegisteredCourses(models.Model):
    user_name = models.CharField(max_length=100)
    registered_course = models.CharField(max_length=255)
    
    
    def __str__(self):
        return f"{self.user_name}, {self.registered_course}"
