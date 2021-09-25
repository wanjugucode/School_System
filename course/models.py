
from django.db import models

# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=12,null=True)
    course_code=models.CharField(max_length=12,null=True)
    syllabus=models.CharField(max_length=12,null=True)
    course_trainer=models.CharField(max_length=13,null=True)
    course_duration=models.CharField(max_length=12,null=True)
    course_schedule=models.DateField(null=True)
    
    