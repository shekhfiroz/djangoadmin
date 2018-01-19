from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email_name=models.EmailField()
    salary=models.ImageField()
def __str__(self):
    return self.first_name

#writing Courses
class Courses(models.Model):
    course_name=models.CharField(max_length=20)
    course_duration=models.CharField(max_length=20)
    def __str__(self):
        return self.course_name