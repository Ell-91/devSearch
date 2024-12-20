import email
from django.db import models
from django.contrib.auth.models import User # import django's user model
import uuid


from django.db.models.signals import post_save, post_delete # post_save triggers anytime a model is saved/ after a model is saved
from django.dispatch import receiver #Decorator
# Create your models here. (One to One relationship with the profile mode;)

#User class that inherits from models.Model
#This will extend the user model (replicate User and extend Profile)
# Don't modify user model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  #anytime a user is deleted, the profile is deleted 
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    short_intro = models.CharField(max_length=200, blank=True, null=True, default="This is a default bio. User has not added a bio yet.")
    username = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True, default="Earth")
    bio = models.TextField(blank=True, null= True)
    profile_image = models.ImageField(blank=True, null= True, upload_to='profiles/', default='profiles/user-default.png' ) #route where the profile goes 
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_youtube = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True) #time stamp
    id = models.UUIDField(default=uuid. uuid4, unique=True, primary_key=True, editable=False) # set an id field

    def __str__(self):
        return str(self.user)
        
class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True) #create a parent child relationship (Parent: Profile Model)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True) #time stamp
    id = models.UUIDField(default=uuid. uuid4, unique=True, primary_key=True, editable=False) # set an id field

    def __str__(self):
        return str(self.name)

class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    recipient = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name="messages")
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['is_read', '-created']