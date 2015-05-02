from django.db import models
from django.contrib.auth import User
# Create your models here.

class DIYUser(models.Model):
    user = models.OneToOneFields(User)
    #email = models.CharField(max_lenght = 50)
    def __str__(self):
        return self.user.username 
        
    
    #Here we need to reference a User object + all other data needed.

class ItemService(models.Model):
    owner = models.ForeignKey('DIYUser')
    details = models.TextField()
	

class Offer(models.Model):
    IS = models.ForeignKey('ItemService')
    user = models.ForeignKey('DIYUser')
    
