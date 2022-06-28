from distutils.command.upload import upload
from django.db import models
from django.forms import CharField

# Create your models here.
class Courses(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    fee = models.FloatField()
    cover = models.ImageField(upload_to='school/images/')
    resources = models.URLField(blank=True)
    
    
    def __str__(self):
        return self.name