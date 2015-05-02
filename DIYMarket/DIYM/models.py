from django.db import models
from django.contrib.auth import User


class DIYUser(models.Model):
    user = models.OneToOneFields(User)
    #email = models.CharField(max_lenght = 50)
    def __str__(self):
        return self.user.username 

class ItemService(models.Model):
    owner = models.ForeignKey('DIYUser')
    Name = models.CharField(max_length = 20)
    details = models.TextField()
    date_added = models.DateTimeField()#date added into DB


class Offer(models.Model):
    IS = models.ForeignKey('ItemService')
    user = models.ForeignKey('DIYUser')


class Address(models.Model):
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField(max_length=50)
    street = models.CharField(max_length=50)
    aptnumber = models.IntegerField(max_length=50)
