from django.db import models
from django.contrib.auth.models import User 

class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField( max_length=120)
    zip_code = models.CharField('Zip Code', max_length=120)
    phone = models.CharField('contact phone', max_length=120, blank=True)
    web = models.URLField('Website address', blank=True)
    email_address = models.EmailField('Email Address', blank=True)
    owner = models.IntegerField('Venue Owner ', blank = False, default=1)
    venue_image = models.ImageField(null=True, blank=True, upload_to="images/")
    
    def __str__(self) :
        return self.name
    

class MyClubUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue, blank=True, null = True, on_delete=models.CASCADE)
    # manager = models.CharField(max_length=120)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUser, blank=True)

    def __str__(self):
        return self.name

# Create your models here.
