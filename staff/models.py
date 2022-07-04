from django.db import models


# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=100)
    expertise = models.CharField(max_length=250)
    email = models.EmailField()
    contact = models.IntegerField()
    experience = models.IntegerField()
    image = models.ImageField(upload_to='staff/images/')


    def __str__(self):
        return self.name
