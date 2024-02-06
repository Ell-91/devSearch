from django.shortcuts import render, redirect
from .models import Project, Tag
from . forms import ProjectForm, ReviewForm
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .utils import searchProjects, paginateProjects

def projects(request):
    projects, search_query = searchProjects(request)

    custom_range, projects =  paginateProjects(request, projects, 6)

    context =  {'projects': projects, 'search_query': search_query, 'custom_range':custom_range }
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id = pk)
    # tags = project.tags.all()
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()

        projectObj.getVoteCount

        messages.success(request, 'Your review was successfully submitted!')
        return redirect('project', pk=projectObj.id)

    return render(request, 'projects/single-project.html', {'project': projectObj, 'form': form})

@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()

    #once a form is sucessfully submitted we want to redirect and send them to the
    if request.method == 'POST':
        print(request.POST)
        form = ProjectForm(request.POST, request.FILES) #instantiate form class and pass in data
        if form.is_valid(): #checks if all required fields are valid 
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('account') # form successfully submitted, redirect people to the projects page

    context = {'form' : form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url="login")
def updateProject(request, pk):
    #allows only the oiwner of the project to delete
    profile = request.user.profile
    project = profile.project_set.get(id = pk)
    form = ProjectForm(instance = project)

    #once a form is sucessfully submitted we want to redirect and send them to the
    #projects page
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance = project)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url="login")
def deleteProject(request, pk):
    #allows only the oiwner of the project to delete
    profile = request.user.profile
    project = profile.project_set.get(id=pk) #get object by id/primary key   // here we query the object or the project
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project} #pass that into the context dictionary as an object
    return render(request, 'delete_template.html', context )