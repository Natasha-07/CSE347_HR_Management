from django.db import models

class Venue(models.Model):
    name = models.CharField('Venue Nmae', max_length=120)
    address = models.CharField(max_lengt=300)
    area_code = models.CharField('Area code', max_length=10)
    phone = models.CharField('Contact number', max_lengt=25)
    web = models.URLField('Web Address')
    email_address = models.EmailField('Email Address')

    def __str__(self):
        return self.name

class MyClubUser(models.Model):
    first_name = models.CharField(max_lengt=30)
    last_name = models.CharField(max_lengt=30)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Event(models.Model):
    name = models.CharField('Event name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    #venue = models.CharField(max_length=120)
    manager = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUser, blank=True)
    def __str__(self):
        return self.name