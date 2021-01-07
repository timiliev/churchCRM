from django.db import models
import datetime

# Create your models here.
class Member(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        )
    
    MARITAL_STATUS = (
        ('Single', 'Single'),
        ('Married', 'Married'),
        )

    firstName = models.CharField(max_length=100, null=True)
    lastName = models.CharField(max_length=100, null=True)
    workplace = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    street_address = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=10, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    birthday = models.DateField(null=True)
    marital_status = models.CharField(max_length=10, null=True, choices=MARITAL_STATUS)
    membership_status = models.BooleanField(null=True)
    gender = models.CharField(max_length=10, null=True, choices=GENDER)
    date_created = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(null=True, blank=True)

    def __str__(self):
        return (self.firstName + " " + self.lastName)

    
class Event(models.Model):
    name = models.CharField(max_length=200, null=True)
    date = models.DateField(null=True)
    location = models.CharField(max_length=200, null=True)
    attendees = models.ManyToManyField(Member)
    event_picture = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
        

class Group(models.Model):
    name = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(null=True)
    members = models.ManyToManyField(Member)
    group_picture = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name