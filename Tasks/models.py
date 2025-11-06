from django.db import models
from django.contrib.auth.models import User



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
    catagory =models.ForeignKey(Catagory,on_delete=models.CASCADE,related_name='event')
    participants   = models.ManyToManyField(User,related_name="rsvp_event",blank=True)
    photo = models.ImageField(upload_to='event_img',blank=True,null=True,default='event_img/20943471.jpg')
    def __str__(self):
        return self.name





class RSVP(models.Model):
    STATUS_CHOICES = [
        ('going', 'Going'),
        ('not_going', 'Not Going'),
        ('interested', 'Interested'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_rsvps')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_rsvps')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='interested')
    rsvp_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.event.name} ({self.status})"
    



    





