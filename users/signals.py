from django.db.models.signals import post_save, post_delete # post_save triggers anytime a model is saved/ after a model is saved
from django.dispatch import receiver

from django.contrib.auth.models import User # import django's user model
from .models import Profile

from django.core.mail import send_mail
from django.conf import settings


    #model that sends that actually sends this, insance/ object that triggered this, created: T/F valuse that 
    # lets you know if a model/new record was added to the database

#  create some kind of receiver and sender that's going to fire off anytime the save method is called on the user profile.
# @receiver(post_save, sender=Profile) --> this is a decorator
# listener
def createProfile(sender, instance, created, **kwargs): #instance is the instance/model that actually sent this, created a boolen that lets us know if a new record in the database was added or not 
    print('Profile triugggered')
    if created: #first instance of this user
        user = instance # user is going to be the instance, the instance is the sender 
        profile = Profile.objects.create(
            user = user,
            username= user.username,
            email = user.email,
            name= user.first_name,
        ) #create a profile

        #set the user to the user instance

        subject = 'Welcome to DevSearch'
        message = 'We are glad you are here!'

        try:
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [profile.email],
                fail_silently=False,
            )
        except:
            print('Email failed to send...')

def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user

    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()
        
# anytime we delete a profile, we delete a user 
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()
#Signals
# Post save triggers the createProfile method up top to update, post save is called anytime we create a User
post_save.connect(createProfile, sender=User) # anytime a user model gets created, a profile will get created.
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteUser, sender=Profile) # triggers any time a userProfile is deleted 