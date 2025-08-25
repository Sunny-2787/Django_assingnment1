from django.db import models

# Create your models here.

class Catagory(models.Model):
    C_name =models.CharField(max_length=50 ,blank=False,null=False)
    C_Description = models.TextField()
    
    def __str__(self):
        return self.C_name
    
class Event(models.Model):
    name = models.CharField(max_length=10)
    description=models.TextField()
    date = models.DateField()
    time =models.TimeField(blank=True,null=True)
    location =models.CharField(max_length=50)
    catagory =models.ForeignKey(Catagory,on_delete=models.CASCADE,related_name='events')

    def __str__(self):
        return self.name


class Participant(models.Model):
    p_name = models.CharField(max_length=50)

    p_email  =models.EmailField(max_length=254,unique=True)
    events = models.ManyToManyField(Event,related_name='participants')

    def __str__(self):
        return self.p_name

