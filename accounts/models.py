from django.db import models

# Create your models here.
class UserRegCourses(models.Model):
    field_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=100)
    registered_course = models.CharField(max_length=255)
    
    
    def __str__(self):
        return f"{self.user_name}, {self.registered_course}"
