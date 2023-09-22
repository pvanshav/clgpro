from django.db import models

# Create your models here.

class Items(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    disc=models.TextField()

    def __str__(self):
        return self.name
class Forms(models.Model):
    name = models.CharField(max_length=250, unique=True)
    dob = models.DateField()
    age = models.PositiveIntegerField(blank=True)
    gender = models.CharField(max_length=250)
    contact = models.IntegerField()
    email = models.EmailField(max_length=250)
    address = models.CharField(max_length=250)
    department = models.CharField(max_length=250)
    course = models.CharField(max_length=250)


    def __str__(self):
        return self.name