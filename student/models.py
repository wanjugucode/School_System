from django.db import models
import datetime

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=12,null=True)
    last_name=models.CharField(max_length=12,null=True)
    age=models.PositiveSmallIntegerField(null=True,blank=True)
    date_of_birth=models.DateField(max_length=10,null=True)
    roll_number=models.CharField(max_length=10,null=True)
    student_email=models.EmailField(max_length=25,null=True)
    nationality_choices=(
        (u'K', 'Kenyan'),
         (u'U', 'Ugandan'),
          (u'R', 'Rwandan'),
    )
    nationality=models.CharField(max_length =23,choices=nationality_choices, null=True)
    sudent_id=models.CharField(max_length=18, null=True)
    id_number=models.CharField(max_length=18, null=True)
    Gendar_choices=(
        (u'M','Male'),
        (u'F','Female'),
        (u'O','Others'),
    )
    gender=models.CharField(max_length=6,choices=Gendar_choices,null=True)
    phone_number=models.CharField(max_length=16,null=True)
    county=models.CharField(max_length=12,null=True)
    profile=models.ImageField(null=True)
    medical_report=models.FileField(null=True)
    date_of_enrollment=models.DateField(max_length=8,null=True)
    course_name=models.CharField(max_length=10,null=True)
    LANGAUAGE_CHOICES=(
        ('E','English'),
        ('k','Kiswahili'),
        ('ki','Kinywaranda'),
    )
    language=models.CharField(max_length=6, choices =LANGAUAGE_CHOICES ,null=True)
    serial_number=models.CharField(max_length=10,null=True)


    def full_name(self):
        return f"{self.first_name} {self.last_name}"    

    def year_of_birth(self):
        current_year=datetime.datetime.now().year
        year=current_year-self.age
        return  year

    
  


