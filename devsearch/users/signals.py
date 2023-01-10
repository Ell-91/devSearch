from django.db.models.signals import post_save, post_delete # post_save triggers anytime a model is saved/ after a model is saved
from django.dispatch import receiver

from django.contrib.auth.models import User # import django's user model
from .models import Profile


    #model that sends that actually sends this, insance/ object that triggered this, created: T/F valuse that 
    # lets you know if a model/new record was added to the database

# @receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, **kwargs): #instance is the instance/model that actually sent this, created a boolen that lets us know if a new record in the database was added or not 
    if created: #first instance of this user
        user = instance # user is going to be the instance, the instance is the sender 
        profile = Profile.objects.create(
            user = user,
            username= user.username,
            email = user.email,
            name= user.first_name,
        ) #create a profile

        #set the user to the user instance

def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()

post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=Profile) # triggers any time a userProfile is deleted 