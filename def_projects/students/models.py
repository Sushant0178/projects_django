from django.db import models

# Create your models here.

class student(models.Model):
    student_id = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=None)


    def __str__(self):
        return self.name