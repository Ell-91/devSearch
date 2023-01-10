from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import Profile #import all profile objects

# Create your views here.
# Create a view for the login page

# def loginPage(request):
#     # When a user submits data we want to ouput certain errors 
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#     return render(request, 'users/login_register.html')

def profiles(request):
    profiles = Profile.objects.all() #import all profile objects
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)
    
    #This info is now available in the template
def userProfile(request, pk):
    profile = Profile.objects.get(id=pk) #import all profile objects

    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    context = {'profile': profile, 'topSkills': topSkills, 'otherSkills': otherSkills}
    return render(request, 'users/user-profile.html', context)