from django.db import models

# Create your models here.

class Trainer(models.Model):
    first_name=models.CharField(max_length=12,null=True)
    last_name=models.CharField(max_length=12,null=True)
    course= models.CharField(max_length=12,null=True)
    GENDER_CHOICES= (
         ('M' ,'Male'),
          ('F' ,'Female'),
           ('O' ,'Others'),
    )
    gender=models.CharField (max_length=1,choices=GENDER_CHOICES,null=True)
    number_of_lessons=models.PositiveBigIntegerField(null=True)
    profile=models.ImageField(null=True)
    occupation=models.CharField(max_length=25,null=True)
    phone_number=models.CharField(max_length=10,null=True)
    bio=models.TextField(null=True)
    cv=models.FileField(null=True)
    email=models.EmailField(null=True)
    contract=models.FileField(null=True)
    date_hired=models.DateField(max_length=10,null=True)
    LANGUAGE_CHOICES=(
        ('E', 'English'),
        ('E', 'Swahili'),
        ('E', 'Kinyarwanda'),
        ('E', 'French'),
        ('E', 'Kiganda'),
   )
    language=models.CharField(max_length=1,choices=LANGUAGE_CHOICES,null=True)
    def full_name(self):
        return f"{self.first_name} {self.last_name}"   
 

   
