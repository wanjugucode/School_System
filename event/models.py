from django.db import models

# Create your models here.
class Event(models.Model):

    title=models.CharField(max_length=100)
    description=models.TextField()
    start_time=models.DateField()
    end_time=models.DateField()
    
    
    

    

    
  


